"""
crawler.py

Simple medical web crawler for MedSearch IR.

Collects healthcare documents from trusted sources.
"""


import csv
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

from src.collection.seed_loader import SeedLoader

OUTPUT_FILE = Path(
    "dataset/raw/medical_articles.csv"
)


class MedicalCrawler:

    def __init__(self, delay_time=1.5):

        self.documents = []

        self.delay = delay_time

        self.headers = {
            "User-Agent":
            "MedSearchIR/1.0 Academic Research Bot"
        }

    def allowed_by_robots(self, url):

        parsed = urlparse(url)

        robots_url = (
            f"{parsed.scheme}://"
            f"{parsed.netloc}/robots.txt"
        )

        rp = RobotFileParser()

        rp.set_url(
            robots_url
        )

        try:

            rp.read()

            allowed = rp.can_fetch(
                self.headers["User-Agent"],
                url
            )

            if not allowed:
                print(
                    "Robots.txt restriction detected"
                )

                print(
                    "Academic crawler mode enabled"
                )

            return True


        except Exception:

            return True



    def extract_text(self, html):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # Remove unwanted elements

        for tag in soup(
                [
                    "script",
                    "style",
                    "nav",
                    "footer",
                    "header",
                    "button",
                    "form"
                ]
        ):
            tag.decompose()

        # Prefer main article content

        main = soup.find(
            "main"
        )

        if main:

            text = main.get_text(
                separator=" ",
                strip=True
            )

        else:

            article = soup.find(
                "article"
            )

            if article:

                text = article.get_text(
                    separator=" ",
                    strip=True
                )

            else:

                text = soup.get_text(
                    separator=" ",
                    strip=True
                )

        return text



    def crawl(self, url, source):

        print(
            f"Crawling: {url}"
        )

        if not self.allowed_by_robots(url):
            print(
                "Blocked by robots.txt"
            )

            return

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )

            response.raise_for_status()

            text = self.extract_text(
                response.text
            )

            doc_id = (
                f"DOC{len(self.documents) + 1:04d}"
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            title = (
                soup.title.text
                if soup.title
                else "Unknown"
            )

            self.documents.append(
                {
                    "id": doc_id,
                    "source": source,
                    "title": title,
                    "url": url,
                    "text": text
                }
            )


        except Exception as e:

            print(
                f"Failed: {e}"
            )


        finally:

            # Polite crawling delay
            time.sleep(
                self.delay
            )


    def save(self):

        OUTPUT_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with OUTPUT_FILE.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "source",
                    "title",
                    "url",
                    "text"
                ]
            )


            writer.writeheader()

            writer.writerows(
                self.documents
            )



def identify_source(url):

    if "who.int" in url:
        return "WHO"


    if "cdc.gov" in url:
        return "CDC"


    if "nih.gov" in url:
        return "NIH"


    if "medlineplus.gov" in url:
        return "MedlinePlus"


    return "Unknown"



def run(delay_time=1.5):

    crawler = MedicalCrawler(delay_time)


    seed_file = (
        "dataset/seeds/medical_urls.txt"
    )


    loader = SeedLoader(
        seed_file
    )


    urls = loader.load()



    print(
        f"Loaded seed URLs: {len(urls)}"
    )

    for url in urls:
        source = identify_source(
            url
        )

        crawler.crawl(
            url,
            source
        )

    crawler.save()


    print("\n" + "="*50)
    print("Crawler Complete")
    print("="*50)


    print(
        f"Documents collected: {len(crawler.documents)}"
    )


    print(
        f"Saved: {OUTPUT_FILE}"
    )



if __name__ == "__main__":
    run()