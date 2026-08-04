"""
Runs the medical crawler pipeline.
"""

import sys
from pathlib import Path


# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


from src.collection.crawler import run



if __name__ == "__main__":

    run()