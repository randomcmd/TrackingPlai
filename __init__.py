"""Top-level package for tracking_plai."""

import os
from pathlib import Path
import sys

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """tracking-plai"""
__email__ = "you@gmail.com"
__version__ = "0.0.1"

from .src.nodes import NODE_CLASS_MAPPINGS
from .src.nodes import NODE_DISPLAY_NAME_MAPPINGS


