"""src/transform_data.py"""

from typing import Any, Callable

from src.transformers.pandas_transform import transform_with_pandas
from src.transformers.polars_transform import transform_with_polars


TRANSFORMER_FUNCS = {
    "pandas": transform_with_pandas,
    "polars": transform_with_polars,
}


def get_transformer_func(
    params: dict[str, Any]
) -> Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]:
    """ """
    # Unpack the paramets
    method = params.get("method", None)

    # Return the extractor function
    return TRANSFORMER_FUNCS[method]
