import os
import sys

# Ensure the repository root is on sys.path so tests can import root modules like student and validation.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
