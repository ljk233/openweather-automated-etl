""" """

import datetime as dt
import os


def check_environment(config):
    """Check if the necessary directories exist."""
    errors = []

    # Check output directory existence
    output_dir = config.get("output", {}).get("directory")
    if output_dir and not os.path.exists(output_dir):
        errors.append(f"Output directory not found: {output_dir}")

    # Check if database file exists
    db_path = config.get("database", {}).get("path")
    if db_path and not os.path.exists(db_path):
        errors.append(f"Database file not found: {db_path}")

    # Check if log directory exists
    log_dir = config.get("logging", {}).get("file")
    if log_dir and not os.path.exists(os.path.dirname(log_dir)):
        errors.append(f"Log directory does not exist: {os.path.dirname(log_dir)}")

    # Check if API key is set
    api_key = config.get("api", {}).get("api_key")
    if not api_key:
        errors.append("API key is not set in the config.")

    # Return all errors
    return errors


def setup_data_storage(
    storage_path: str = "./data", format_str: str = "%Y%m%d%H%M%S"
) -> str:
    """ """
    if not os.path.exists(storage_path):
        raise FileNotFoundError()

    # Construct the destination directoy name
    dest_dir_name = dt.datetime.now().strftime(format_str)

    # Construct the destination director path
    dest_dir_path = os.path.join(storage_path, dest_dir_name)

    # Create the destination directory
    if os.path.exists(dest_dir_path):
        raise FileExistsError()

    os.mkdir(dest_dir_path)

    return dest_dir_path
