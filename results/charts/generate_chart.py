"""
generate_chart.py
Reads results/evaluation_results.csv and generates Figure 4.1 chart.
"""
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# File paths relative to project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CSV_FILE = PROJECT_ROOT / "results" / "evaluation_results.csv"
OUTPUT_IMAGE = PROJECT_ROOT / "results" / "charts" / "chart.png"

def generate_benchmark_chart():
    if not CSV_FILE.exists():
        print(f"Error: Could not find evaluation results at {CSV_FILE}")
        print("Please run 'python scripts/evaluate.py' first.")
        return

    queries = []
    precision = []
    recall = []
    f1 = []
    map_scores = []
    ndcg_scores = []

    # Read evaluation data
    with CSV_FILE.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            queries.append(row["query"])
            precision.append(float(row["precision"]))
            recall.append(float(row["recall"]))
            f1.append(float(row["f1"]))
            map_scores.append(float(row["MAP"]))
            ndcg_scores.append(float(row["nDCG"]))

    if not queries:
        print("Error: No data found in CSV file.")
        return

    # Plot Configuration
    x = range(len(queries))
    width = 0.15

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot bars for each metric
    ax.bar([i - 2 * width for i in x], precision, width, label="Precision", color="#2b5c8f")
    ax.bar([i - width for i in x], recall, width, label="Recall", color="#4682b4")
    ax.bar([i for i in x], f1, width, label="F1 Score", color="#6baed6")
    ax.bar([i + width for i in x], map_scores, width, label="MAP", color="#9ecae1")
    ax.bar([i + 2 * width for i in x], ndcg_scores, width, label="nDCG", color="#c6dbef")

    # Aesthetics and Labels
    ax.set_ylabel("Score", fontsize=12)
    ax.set_title("Figure 4.1: Metric Evaluation Across Benchmark Queries", fontsize=14, fontweight="bold", pad=15)
    ax.set_xticks(list(x))
    ax.set_xticklabels(queries, fontsize=10, rotation=15, ha="right")
    ax.set_ylim(0, 1.1)
    ax.legend(loc="upper right", frameon=True)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    # Ensure output directory exists and save
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT_IMAGE, dpi=300)
    plt.close()

    print("=" * 50)
    print(f"Chart successfully saved to: {OUTPUT_IMAGE}")
    print("=" * 50)

if __name__ == "__main__":
    generate_benchmark_chart()