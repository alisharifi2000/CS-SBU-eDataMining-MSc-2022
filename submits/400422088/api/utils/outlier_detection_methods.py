from utils.common import read_json_time_series
import numpy as np

def outlier_z_score(data, cols):
    for col in cols:
        threshold = 1.5
        mean_y = np.mean(data[col])
        stdev_y = np.std(data[col])
        for i in data.index:
            y = data.loc[i, col]
            z_scores = (y - mean_y) / stdev_y 
            if abs(z_scores) > threshold:
                data.loc[i, "z_score_"+str(col)] = True
            else:
                data.loc[i, "z_score_"+str(col)] = False
    return data  

def outlier_iqr(data, cols):
    for col in cols:
        quartile_1, quartile_3 = np.percentile(data[col], [25, 75])
        iqr = quartile_3 - quartile_1
        lower_bound = quartile_1 - (iqr * 1)
        upper_bound = quartile_3 + (iqr * 1)
        for i in data.index:
            y = data.loc[i, col]
            if (y > upper_bound) | (y < lower_bound):
                data.loc[i, "iqr_"+str(col)] = True
            else:
                data.loc[i, "iqr_"+str(col)] = False
    return data  

def outlier_detection(data, config):
    data = read_json_time_series(data)
    methods = config["methods"]
    cols = config["columns"]
    for method in methods:
        method = method.lower()
        if method == "z_score":
            data = outlier_z_score(data, cols)
        elif method == "iqr":
            data = outlier_iqr(data, cols)
    data = data.drop(columns=cols)
    data = data.to_json()
    return data