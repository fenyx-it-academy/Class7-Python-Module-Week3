import json
from datetime import datetime

def save_file(obj):

    with open(f"{'exchange_rates_' + str(datetime.now())}.json", "w") as f:
        json.dump(obj, f)
