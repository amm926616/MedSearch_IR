"""
crawler.py

Focused web crawler for collecting medical documents.

Collects medical information from trusted sources and
exports them into the standardized CSV format used by MedSearch IR.
"""


import csv
import requests

from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urlparse


class MedicalCrawler:


    OUTPUT_FILE = Path(
        "dataset/raw/medical_articles.csv"
    )


    def __init__(self, urls):

        self.urls = urls

        self.documents = []


    def get_source(self, url):

        """
        Extract website name from URL.
        """

        domain = urlparse(url).netloc


        if "who" in domain:
            return "WHO"

        elif "cdc" in domain:
            return "CDC"

        elif "nih" in domain:
            return "NIH"

        elif "pubmed" in domain:
            return "PubMed"

        else:
            return domain



    def fetch_page(self, url):

        """
        Download webpage content.
        """

        headers = {

            "User-Agent":
                (
                    "Mozilla/5.0 "
                    "(X11; Linux x86_64) "
                    "AppleWebKit/537.36 "
                    "Chrome/120 Safari/537.36"
                )

        }


        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )


        response.raise_for_status()


        return response.text



    def extract_content(self, html):

        """
        Extract title and visible text.
        """

        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        # Remove unnecessary elements

        for element in soup(
            [
                "script",
                "style",
                "nav",
                "footer"
            ]
        ):

            element.decompose()



        title = (
            soup.title.text.strip()
            if soup.title
            else "Unknown"
        )

        content = None

        possible_tags = [

            "article",
            "main",
            "div"

        ]

        for tag in possible_tags:

            content = soup.find(tag)

            if content:
                break

        if content:

            text = " ".join(
                content.stripped_strings
            )

        else:

            text = " ".join(
                soup.stripped_strings
            )


        return title, text



    def crawl(self):

        """
        Crawl all provided URLs.
        """

        for number, url in enumerate(
            self.urls,
            start=1
        ):

            try:

                print(
                    f"Crawling: {url}"
                )


                html = self.fetch_page(
                    url
                )


                title, text = self.extract_content(
                    html
                )


                document = {

                    "id":
                    f"DOC{number:04}",

                    "source":
                    self.get_source(url),

                    "title":
                    title,

                    "url":
                    url,

                    "text":
                    text

                }


                self.documents.append(
                    document
                )


            except Exception as error:

                print(
                    f"Failed: {url}"
                )

                print(error)



    def save_csv(self):

        """
        Save collected documents.
        """


        self.OUTPUT_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with self.OUTPUT_FILE.open(
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



        print()
        print("=" * 50)
        print("Crawler Complete")
        print("=" * 50)
        print(
            f"Documents collected: {len(self.documents)}"
        )

        print(
            f"Saved: {self.OUTPUT_FILE}"
        )



    def run(self):

        self.crawl()

        self.save_csv()



def main():

    sources = [

        "https://www.who.int/news-room/fact-sheets/detail/tuberculosis",

        "https://www.nhlbi.nih.gov/health/high-blood-pressure",

        "https://www.nhlbi.nih.gov/health/coronary-heart-disease"

    ]


    crawler = MedicalCrawler(
        sources
    )


    crawler.run()



if __name__ == "__main__":

    main()