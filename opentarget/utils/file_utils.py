import os

def ensure_data_dir():
    """Ensure the data directory exists."""
    if not os.path.exists("data"):
        os.makedirs("data")