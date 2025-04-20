import os
import json
import requests
from opentarget.utils.file_utils import ensure_data_dir

def fetch_or_load(handler):
    ensure_data_dir()
    filename = f"data/{handler.id}_{handler.__class__.__name__.lower()}.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f"🔄 Loaded cached data from {filename}")
            return json.load(f)

    # Build request from handler
    req = handler.get_url()
    response = requests.post(req["url"], json=req["json"])
    response.raise_for_status()
    data = response.json()

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
        print(f"✅ Fetched and saved new data to {filename}")

    return data