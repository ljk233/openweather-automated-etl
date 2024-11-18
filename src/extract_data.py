"""src/extract_data.py"""

from typing import Any, Callable

from src.extractors.extract_api import extract_from_api
from src.extractors.extract_json import extract_from_json

# fetch_from_json


EXTRACTOR_FUNCS = {
    "api": extract_from_api,
    "json": extract_from_json,
}


def get_extractor_func(params: dict[str, Any]) -> Callable[[], dict[str, Any]]:
    """ """
    # Unpack the paramets
    method = params.get("method", None)
    method_params = params.get(method, None)

    # Return the extractor function
    return EXTRACTOR_FUNCS[method](method_params)
