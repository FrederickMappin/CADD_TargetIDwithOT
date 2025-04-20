import os
import json
import requests
from opentarget.handlers.associated_targets import AssociatedTargetsHandler
from opentarget.handlers.associated_diseases import AssociatedDiseasesHandler
from opentarget.handlers.target_disease_evidence import TargetDiseaseEvidenceHandler

HANDLERS = {
    "associated_targets": AssociatedTargetsHandler,
    "associated_diseases": AssociatedDiseasesHandler,
    "target_disease_evidence": TargetDiseaseEvidenceHandler,
}

def handler_factory(request_type: str, id: str):
    """Returns the appropriate handler class based on request_type."""
    try:
        return HANDLERS[request_type](id)
    except KeyError:
        raise ValueError(f"Unsupported request type: {request_type}")

def fetch_or_load(handler):
    ensure_data_dir()
    # Debugging: Print handler details
    print(f"Handler instance: {handler}")
    print(f"Handler class name: {handler.__class__.__name__}")
    
    # Construct the filename with handler information
    handler_class_name = handler.__class__.__name__.lower()
    filename = f"data/{handler.id}_{handler_class_name}.json"
    print(f"Filename being used: {filename}")

    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f"🔄 Loaded cached data from {filename}")
            return json.load(f)

    # Build request from handler
    req = handler.get_url()
    response = requests.post(req["url"], json=req["json"])
    response.raise_for_status()
    data = response.json()

    # Save the fetched data to the constructed filename
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
        print(f"✅ Fetched and saved new data to {filename}")

    return data