"""Top-level package for tracking_plai."""

import os
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]

print(f'{PROJECT_ROOT=}')

if PROJECT_ROOT not in sys.path:
    print("Appending project root to sys path")
    sys.path.append(PROJECT_ROOT)

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """tracking-plai"""
__email__ = "you@gmail.com"
__version__ = "0.0.1"

from .src.tracking_plai.nodes import NODE_CLASS_MAPPINGS
from .src.tracking_plai.nodes import NODE_DISPLAY_NAME_MAPPINGS


