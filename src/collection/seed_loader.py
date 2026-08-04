"""
seed_loader.py

Loads crawler seed URLs from a text file.
"""


from pathlib import Path



class SeedLoader:


    def __init__(self, seed_file):

        self.seed_file = Path(seed_file)



    def load(self):

        if not self.seed_file.exists():

            raise FileNotFoundError(
                f"Seed file not found: {self.seed_file}"
            )


        urls = []


        with self.seed_file.open(
            "r",
            encoding="utf-8"
        ) as file:


            for line in file:

                url = line.strip()


                # Ignore empty lines
                # Ignore comments

                if (
                    url
                    and
                    not url.startswith("#")
                ):

                    urls.append(url)


        return urls