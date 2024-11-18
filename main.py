"""main.py"""

from src.config import load_config
from src.flow import run_flow


CONFIG_FILE_PATH = "./config/config.yaml"


def main(config_file_path: str):
    """ """
    # Load the configuration file
    config = load_config(config_file_path)

    # Run the pipeline
    output = run_flow(config)

    print(output)


if __name__ == "__main__":
    main(CONFIG_FILE_PATH)
