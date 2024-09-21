import os
from pathlib import Path


VERSION = "0.2.1"
FFORMAT = ".Spe"
OUTPUT_FORMAT = ".csv"


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = BASE_DIR / "output"

if not os.path.isdir(DEFAULT_OUTPUT_DIR):
    os.mkdir(DEFAULT_OUTPUT_DIR)