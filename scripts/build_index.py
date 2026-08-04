"""
Builds search index and metadata.
"""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


from src.indexing.index_builder import run as build_index
from src.indexing.metadata import run as build_metadata



if __name__ == "__main__":

    build_index()

    build_metadata()