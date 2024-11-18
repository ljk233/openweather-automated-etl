"""src/extractors/extract_api.py"""

from typing import Any, Callable

import requests


def extract_from_api(params: dict[str, Any]) -> Callable[[], dict[str, Any]]:
    """ """
    # Unpack the parameters
    base_url = params["base_url"]
    request_parameters = params["parameters"]

    def extract_data() -> dict[str, Any]:
        """ """
        response = requests.get(base_url, params=request_parameters)
        if response.status_code == 200:
            return response.json()

        raise ValueError(
            f"API request to {response.url} failed with status code {response.status_code}: {response.text}"
        )

    return extract_data
