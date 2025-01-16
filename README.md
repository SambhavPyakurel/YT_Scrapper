# YouTube Scrapper

This script extracts data from a specified YouTube channel using the YouTube Data API v3. It gathers information such as video URLs, thumbnails, titles, views, and upload times of the latest videos and saves it into a CSV file.

## Features

1. Extracts the following details for the latest 5 videos on a YouTube channel:
   - **Video URLs**
   - **Thumbnail URLs**
   - **Video Titles**
   - **View Counts**
   - **Upload Times**
2. Saves the extracted data into a CSV file (`storage.csv`) for easy analysis and visualization.

## Requirements

- Python 3.x
- `google-api-python-client`

## Installation

1. Clone the repository or download the script.
2. Install the required Python package:
   ```bash
   pip install google-api-python-client
   ```

## Usage

1. Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
2. Replace `YOUR_API_KEY` with your actual API key.
3. Replace `CHANNEL_ID` with the YouTube channel ID you want to analyze.
4. Run the script:
   ```bash
   python script_name.py
   ```

## Output

The script generates a `storage.csv` file with the following columns:

| Video URL                        | Thumbnail URL                   | Video Title             | Views  | Upload Time          |
|----------------------------------|---------------------------------|-------------------------|--------|----------------------|
| https://www.youtube.com/watch?v= | https://i.ytimg.com/vi/...      | Example Title           | 12345  | 2025-01-01T00:00:00Z|

## Notes

- Ensure that your API key has the appropriate permissions to access the YouTube Data API.
- The `maxResults` parameter is set to 5 but can be adjusted as needed.
- Modify the script as necessary to suit your specific use case.
