import numpy as np


def outlier_z_score(data, cols):
    for col in cols:
        threshold = 1.5
        mean = np.mean(data[col])
        std = np.std(data[col])
        for i in data.index:
            feature = data.loc[i, col]
            z_scores = (feature - mean) / std
            data.loc[i, "z_score_"] = z_scores > threshold or z_scores < -threshold
    return data


def outlier_percentile(data, cols):
    for col in cols:
        q1, q3 = np.percentile(data[col], [25, 75])
        diff = q3 - q1
        lower_bound = q1 - (diff * 1)
        upper_bound = q3 + (diff * 1)
        for i in data.index:
            y = data.loc[i, col]
            data.loc[i, "percentile_"] = y < lower_bound or y > upper_bound
    return data


def outlier_detection(data, config):
    columns = data.columns.to_list()
    if 'time' in columns:
        columns.remove('time')
    if 'id' in columns:
        columns.remove('id')
    # iqr - percentile
    data.percentile = outlier_percentile(data, columns)
    # z_score
    data.z_score = outlier_z_score(data, columns)

    return data
