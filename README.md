# OpenWeather ETL Pipeline

## Overview

This project is an automated ETL (Extract, Transform, Load) pipeline designed to collect weather data from the OpenWeather API, clean and process the data, and store it in a local SQLite3 database. The pipeline is modular, efficient, and designed for scalability.

## Features

- **Automated Data Retrieval**: Fetches weather data periodically from the OpenWeather API.
- **Efficient Data Transformation**: Cleans and processes data using Polars, a high-performance DataFrame library.
- **Schema Validation**: Ensures data integrity with Pandera.
- **Local Storage**: Saves processed data into a SQLite3 database for analysis or reporting.
- **Custom Configuration**: Easily configure API keys, database settings, and pipeline behavior.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up configuration**
   - Rename the example config file and update it with your details:

```bash
cp config/config.example.yaml config/config.yaml
```

- Add your OpenWeather API key and database path.

## Usage

1. **Run the pipeline**

```bash
python src/main.py
```

2. **Schedule periodic runs**

Use a scheduler like `cron` or `APScheduler` for automation.

## Configuration

The pipeline uses a YAML configuration file located at `config/config.yaml`.
Key parameters include:

- **API Settings**:

```yaml
api:
  url: "https://api.openweathermap.org/data/2.5/weather"
  key: "your_api_key_here"
```

- **Database Settings**:

```yaml
database:
  connection_string: "sqlite:///weather_data.db"
```

## Project Structure

```plain
etl_project/
├── README.md                # Project overview and instructions
├── requirements.txt         # Python dependencies
├── config/
│   ├── config.yaml          # Configuration file for API keys, database URLs, etc.
│   └── logging.conf         # Logging configuration
├── data/                    # Folder for temporary data storage (optional)
├── src/
│   ├── __init__.py          # Makes src a package
│   ├── extract.py           # Functions for data extraction
│   ├── transform.py         # Functions for data transformation
│   ├── load.py              # Functions for data loading
│   ├── utils.py             # Helper functions (e.g., error handling, logging)
│   └── main.py              # Entry point for running the ETL pipeline
├── tests/                   # Unit and integration tests
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_end_to_end.py   # End-to-end testing for the ETL process
└── logs/
    └── etl.log              # Log file for ETL execution
```

## Dependencies

See `requirements.txt` for the full list of dependencies.
Core libraries include:

- [Polars](https://www.pola.rs/) for data manipulation.
- [Pandera](https://pandera.readthedocs.io/) for schema validation.
- [SQLAlchemy](https://www.sqlalchemy.org/) for database interaction.
- [Requests](https://docs.python-requests.org/) for API calls.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
