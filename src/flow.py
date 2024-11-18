"""src/flow.py"""

import os
from typing import Any

from src.extract_data import get_extractor_func
from src.transform_data import get_transformer_func
from src.shared import setup_data_storage, write_to_json


def run_flow(config: dict[str, Any]):
    """ """
    # 1. Setup the intermediate data storage
    # data_storage_params = config.get("data_storage", {})
    # data_dir = data_storage_params.get("data_dir", None)
    # data_dir_template = data_storage_params.get("data_dir_template", None)
    # dest_dir_path = setup_data_storage(data_dir, data_dir_template)

    # 2. Extract the data
    # raw_data_file_name = data_storage_params.get("raw_data", None)
    extract_data_params = config.get("extract_data", {})
    raw_data = extract(extract_data_params)

    # 2. Transform the data
    transform_data_params = config.get("transform_data", {})
    cleansed_data = transform(raw_data, transform_data_params)

    # 3. Load the data

    return cleansed_data


def extract(params: dict[str, Any]) -> dict[str, Any]:
    """ """
    # Get the transformer function
    extractor_func = get_extractor_func(params)

    # Extract the data
    return extractor_func()


def transform(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
    """ """
    # Get the transformer function
    transformer_func = get_transformer_func(params)

    # Extract the data
    return transformer_func(data, params)
