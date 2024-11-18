""" """

from typing import Any

import pandas as pd


def transform_with_pandas(
    data: dict[str, Any], params: dict[str, Any]
) -> dict[str, Any]:
    """ """
    return pd.DataFrame([data])
