#!/usr/bin/python3
# 6-load_from_json_file.py
# A Python program that demostrate loading from JSON file
"""Defines a loading JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
