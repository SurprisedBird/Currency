import os
from pathlib import Path

BASE_DIR = os.path.dirname(__file__)
BASE_DIR2 = Path(__file__).resolve().parent.parent
print(BASE_DIR)
print(BASE_DIR2)
