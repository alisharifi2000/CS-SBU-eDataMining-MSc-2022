from utils.common import read_json_time_series

def manage(data, config):
    data = read_json_time_series(data)
    major_class = config["major_class"]
    minor_class = config["minor_class"]
    method = config["method"]
    method = method.lower()
    return "ok"