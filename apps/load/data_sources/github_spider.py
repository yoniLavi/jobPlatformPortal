import logging
import requests

GITHUB_FILE_LISTING_ENDPOINT = "https://api.github.com/repos/ryanom/job-openings-git-scraper/git/trees/main?recursive=1"
RAW_FILE_ENDPOINT_BASE = "https://raw.githubusercontent.com/RyanOM/job-openings-git-scraper/main"


def load_github_spider_results():

    data_source_url = "https://github.com/RyanOM/job-openings-git-scraper/tree/main/data"
    logging.info(f"Loading Github Spider data from {data_source_url}")

    # TODO - This needs to be implemented
    # Steps:
    # 1. Get listing of the files on the github repo
    file_listing = fetch_github_file_listing(GITHUB_FILE_LISTING_ENDPOINT)
    datasets = get_json_datasets(file_listing)
    # 2. Request the files from github as if they were an API
    # 3. Parse the files and load them into the database
    return datasets


def fetch_github_file_listing(endpoint):
    """Fetch json file listing from GitHub repo"""
    resp = requests.get(endpoint)
    resp.raise_for_status()
    return resp.json()


def get_json_datasets(file_listing):
    """Retrieve JSON datasets results from GitHub spider"""
    return [
        f'{RAW_FILE_ENDPOINT_BASE}/{record["path"]}'
        for record in file_listing["tree"]
        if record["path"].startswith("data/") and record["path"].endswith(".json")
    ]

    

if __name__ == "__main__":
    print(load_github_spider_results())