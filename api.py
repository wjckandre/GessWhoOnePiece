import requests
import json
from apify_client import ApifyClient


# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_9gZzidPty5A5yEWeUHhqkau6tdaiw04kFAeX")

characters = requests.get("https://api.api-onepiece.com/v2/characters/fr").json()
print(characters[0]["name"])
print(len(characters))

def get_image(name):
    # Prepare the Actor input
    run_input = { "queries": [name], "maxResultsPerQuery": 1 }

    # Run the Actor and wait for it to finish
    run = client.actor("hooli/google-images-scraper").call(run_input=run_input)


    # Fetch and print Actor task results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        return item
