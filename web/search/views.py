import sys
import time
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# 1. Add project root (MedSearch_IR) to sys.path so we can import `src`
BASE_DIR = Path(__file__).resolve().parent.parent  # web/
PROJECT_ROOT = BASE_DIR.parent                     # MedSearch_IR/

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.query.search_engine import SearchEngine


# 2. Global SearchEngine instance
search_engine = None
try:
    search_engine = SearchEngine()
except Exception as e:
    print(f"Warning: Could not initialize SearchEngine: {e}")


def search_page(request):
    """Main search landing page"""
    return render(request, "search/search.html")


def search_api(request):
    """HTMX endpoint for search queries"""
    query = request.GET.get("query", "").strip()

    if not query:
        return HttpResponse(
            '<div class="empty-state">'
            '<div class="empty-state-icon">🔍</div>'
            '<p>Enter a medical query to start searching</p>'
            '</div>'
        )

    if query.lower() in ["exit", "quit", "q"]:
        return HttpResponse(
            '<div class="goodbye-message">'
            '<div class="goodbye-icon">👋</div>'
            '<p>Thank you for using MedSearch IR!</p>'
            '</div>'
        )

    if not search_engine:
        return HttpResponse(
            '<div class="error-state">'
            '<div class="error-icon">⚠️</div>'
            '<p>Search Engine failed to load.</p>'
            '</div>'
        )

    try:

        start_time = time.perf_counter()

        raw_results = search_engine.search(
            query,
            top_k=5
        )

        elapsed_time = (
            time.perf_counter() - start_time
        ) * 1000


        search_engine.save_history(
            query,
            raw_results
        )


        formatted_results = []

        query_terms = query.split()


        for rank, (doc_id, score) in enumerate(
            raw_results,
            start=1
        ):

            doc_meta = search_engine.metadata.get(
                doc_id,
                {}
            )

            doc_full = search_engine.documents.get(
                doc_id,
                {}
            )


            snippet = search_engine.generate_snippet(
                doc_full.get("text", ""),
                query_terms
            )


            formatted_results.append({

                "rank": rank,
                "id": doc_id,

                "title": doc_meta.get(
                    "title",
                    "Untitled Document"
                ),

                "source": doc_meta.get(
                    "source",
                    "Unknown Source"
                ),

                "url": doc_meta.get(
                    "url",
                    "#"
                ),

                "score": f"{score:.4f}",

                "snippet": snippet,
            })


        html = render_to_string(
            "search/partials/results.html",
            {
                "query": query,
                "results": formatted_results,
                "result_count": len(formatted_results),

                "processing_time":
                    round(elapsed_time, 2),

                "total_documents":
                    len(search_engine.documents),

                "ranking_model":
                    "BM25",
            }
        )

        return HttpResponse(html)


    except Exception as e:

        return HttpResponse(
            f"""
            <div class="error-state">
                <div class="error-icon">⚠️</div>
                <p>An error occurred while searching:
                {str(e)}</p>
            </div>
            """
        )