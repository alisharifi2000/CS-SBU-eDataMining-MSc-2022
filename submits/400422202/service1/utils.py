import pandas as pd
from utils.common import convert_shamsi_to_miladi


def read_json_time_series(data, config):
    error = None
    try:
        type = config['type']
    except Exception:
        error = "config type should be provided"
        return data, error
    if type == "shamsi":
        convert_shamsi_to_miladi(data)
    data = pd.DataFrame(data=data)
    data.time = pd.to_datetime(data.time,)
    return data, error
