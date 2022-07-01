import pandas as pd

def read_json_time_series(data, config):
    error = None
    data = pd.DataFrame(data=data)
    try:
        data.time = pd.to_datetime(data.time)
    except Exception as error:
        return data, str(error)
    return data, error
