import logging

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE

from common import prepare_data


class ImbalancedClassification:

    def __init__(self, serlializer_data):
        self.balanced_data = self.balance_data(serlializer_data)

    def balance_data(self, serializer_data):
        """Call outlier detection methods in order to add method columns"""
        logging.critical(serializer_data)
        df_data, config = prepare_data(serializer_data)

        assert config.get('method') is not None
        df_data = getattr(self, config.get('method').lower())(df_data)

        return df_data.to_dict()

    @staticmethod
    def undersampling(df_data):
        """Delete major class samples randomly"""
        nmin = df_data['class'].value_counts().min()
        df_data = df_data.groupby('class').apply(lambda x: x.sample(nmin)).reset_index(drop=True)

        return df_data

    @staticmethod
    def oversampling(df_data):
        """Duplicate minor class samples randomly"""
        nmax = df_data['class'].value_counts().max()

        lst = [df_data]
        for class_index, group in df_data.groupby('class'):
            sample = group.sample(nmax - len(group), replace=True)
            lst.append(sample)

        df_data = pd.concat(lst).reset_index(drop=True)

        return df_data

    @staticmethod
    def smote(df_data):
        """Balance imbalanced classification data using SMOTE method"""
        nmin = df_data['class'].value_counts().min()

        x = df_data.drop(['class', 'id'], axis=1)
        y = df_data['class']

        sm = SMOTE(k_neighbors=nmin - 1)

        columns_names = x.columns
        feature_count = len(x.columns)
        if feature_count == 1:
            x = np.array(x).reshape(-1, 1)
        try:
            x_smote, y_smote = sm.fit_resample(
                x,
                y
            )
        except ValueError:
            raise ValueError('Minor class should contain more than one member')

        if feature_count == 1:
            x_smote = pd.DataFrame(x_smote, columns=columns_names)
        frames = [
            x_smote,
            y_smote
        ]
        df_smote = pd.concat(frames, axis=1)
        df_smote['id'] = range(len(df_smote))

        return df_smote
