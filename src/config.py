""" """

from typing import Any

from src.shared import read_yaml


def load_config(fp: str, stage: str = None) -> dict[str, Any]:
    """Load YAML configuration from a file."""
    config_file = read_yaml(fp)

    if not stage:
        return config_file

    stage_config = config_file.get(stage, None)
    if not stage_config:
        raise ValueError(
            f"Configuration for stage {stage} not found. Possible stages are: {config_file.keys()}"
        )

    return stage_config
