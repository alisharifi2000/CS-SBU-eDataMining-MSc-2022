from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd


def manage_imbalance(data, config):
    df = pd.DataFrame(data)
    if config['method'] == 'SMOTE':
        min_neighbors = df['class'].value_counts().values[-1]
        if min_neighbors <= 1:
            df = pd.concat([df, df]).reset_index().drop('index', axis=1)
        sampler = SMOTE(k_neighbors=min(min_neighbors, 6))

    elif config['method'] == 'OverSampling':
        sampler = RandomOverSampler(random_state=1)

    elif config['method'] == 'UnderSampling':
        sampler = RandomUnderSampler(random_state=1)
    else:
        raise IndexError('Invalid method')

    X, y = sampler.fit_resample(df.drop(['class', 'id'], axis=1), df['class'])
    X['class'] = y
    X['id'] = X.index.to_numpy() + 1

    out = pd.DataFrame(X, columns=df.columns)
    return out

