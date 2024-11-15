
# OpenWeather API Data Dictionary

This document describes the fields returned by the OpenWeather API.

## Fields Overview

| Field Name        | Type    | Description                               | Unit/Format         | Possible Values          |
| ----------------- | ------- | ----------------------------------------- | ------------------- | ------------------------ |
| `lat`             | float   | Latitude of the location.                 | Degrees (−90; 90)   | -90 to 90                |
| `lon`             | float   | Longitude of the location.                | Degrees (−180; 180) | -180 to 180              |
| `timezone`        | string  | Timezone name for the requested location. | -                   | e.g., "America/New_York" |
| `timezone_offset` | integer | Shift in seconds from UTC.                | Seconds             | -43200 to 43200          |

### Current Weather Data (`current`)

| Field Name   | Type    | Description                                  | Unit/Format                    | Possible Values                    |
| ------------ | ------- | -------------------------------------------- | ------------------------------ | ---------------------------------- |
| `dt`         | integer | Current time (Unix timestamp, UTC).          | Unix Timestamp                 | -                                  |
| `sunrise`    | integer | Sunrise time (Unix timestamp, UTC).          | Unix Timestamp                 | -                                  |
| `sunset`     | integer | Sunset time (Unix timestamp, UTC).           | Unix Timestamp                 | -                                  |
| `temp`       | float   | Temperature at the location.                 | Kelvin, Celsius, or Fahrenheit | See unit conversion table below    |
| `feels_like` | float   | Human perception of the temperature.         | Kelvin, Celsius, or Fahrenheit | See unit conversion table below    |
| `pressure`   | float   | Atmospheric pressure at sea level.           | hPa                            | -                                  |
| `humidity`   | float   | Relative humidity percentage.                | %                              | 0-100                              |
| `dew_point`  | float   | Temperature at which dew forms.              | Kelvin, Celsius, or Fahrenheit | See unit conversion table below    |
| `clouds`     | float   | Percentage of cloud cover.                   | %                              | 0-100                              |
| `uvi`        | float   | UV index for the location.                   | Index                          | 0-11 (scale)                       |
| `visibility` | float   | Visibility in meters.                        | meters                         | -                                  |
| `wind_speed` | float   | Wind speed at the location.                  | m/s, km/h, or mph              | -                                  |
| `wind_deg`   | integer | Wind direction, in degrees (meteorological). | Degrees                        | 0-360                              |
| `rain`       | object  | Precipitation volume for the last hour.      | mm/h                           | -                                  |
| `snow`       | object  | Snowfall volume for the last hour.           | mm/h                           | -                                  |
| `weather`    | array   | Weather conditions for the location.         | -                              | See weather conditions table below |

### Forecast Data

#### Minute Forecast (`minutely`)

| Field Name      | Type    | Description                                        | Unit/Format    | Possible Values |
| --------------- | ------- | -------------------------------------------------- | -------------- | --------------- |
| `dt`            | integer | Time of the forecasted data (Unix timestamp, UTC). | Unix Timestamp | -               |
| `precipitation` | float   | Precipitation in mm per hour.                      | mm/h           | -               |

#### Hourly Forecast (`hourly`)

| Field Name   | Type    | Description                                        | Unit/Format                    | Possible Values                 |
| ------------ | ------- | -------------------------------------------------- | ------------------------------ | ------------------------------- |
| `dt`         | integer | Time of the forecasted data (Unix timestamp, UTC). | Unix Timestamp                 | -                               |
| `temp`       | float   | Temperature for the hour.                          | Kelvin, Celsius, or Fahrenheit | See unit conversion table below |
| `feels_like` | float   | Perceived temperature for the hour.                | Kelvin, Celsius, or Fahrenheit | See unit conversion table below |
| `pressure`   | float   | Atmospheric pressure at sea level.                 | hPa                            | -                               |
| `humidity`   | float   | Relative humidity percentage.                      | %                              | 0-100                           |
| `uvi`        | float   | UV index for the hour.                             | Index                          | 0-11 (scale)                    |
| `wind_speed` | float   | Wind speed during the hour.                        | m/s, km/h, or mph              | -                               |
| `wind_deg`   | integer | Wind direction during the hour.                    | Degrees                        | 0-360                           |
| `rain`       | object  | Precipitation volume for the hour.                 | mm/h                           | -                               |
| `snow`       | object  | Snowfall volume for the hour.                      | mm/h                           | -                               |

#### Daily Forecast (`daily`)

| Field Name | Type    | Description                                                      | Unit/Format                    | Possible Values                    |
| ---------- | ------- | ---------------------------------------------------------------- | ------------------------------ | ---------------------------------- |
| `dt`       | integer | Time of the forecasted data (Unix timestamp, UTC).               | Unix Timestamp                 | -                                  |
| `temp`     | object  | Daily temperature data (morning, day, evening, night, min, max). | Kelvin, Celsius, or Fahrenheit | See unit conversion table below    |
| `humidity` | float   | Relative humidity percentage.                                    | %                              | 0-100                              |
| `pressure` | float   | Atmospheric pressure at sea level.                               | hPa                            | -                                  |
| `weather`  | array   | Weather conditions for the day.                                  | -                              | See weather conditions table below |

### Weather Condition Codes (`weather`)

| Code | Condition Description        |
| ---- | ---------------------------- |
| 200  | Thunderstorm with light rain |
| 300  | Drizzle                      |
| 500  | Light rain                   |
| 600  | Light snow                   |
| 800  | Clear sky                    |
| 801  | Few clouds                   |
| 802  | Scattered clouds             |

### Unit Conversion Table

| Unit        | Kelvin | Celsius | Fahrenheit |
| ----------- | ------ | ------- | ---------- |
| Temperature | K      | °C      | °F         |
| Wind Speed  | m/s    | m/s     | mph        |