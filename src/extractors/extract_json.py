"""src/extractors/extract_json.py"""

import os
from typing import Any, Callable

import json


def extract_from_json(params: dict[str, Any]) -> Callable[[], dict[str, Any]]:
    """ """
    # Unpack the parameters
    file_path = params["file_path"]

    def extract_data() -> dict[str, Any]:
        """ """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON file not found at: {file_path}")

        with open(file_path, "r") as fp:
            return json.load(fp)

    return extract_data
