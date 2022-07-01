import logging

from common import prepare_data, to_jalali


class Interpolation:

    TIMEFRAME_TRANSLATION = {
        'daily': 'D',
        'monthly': 'M',
        'hourly': 'H',
        'minutes': 'T',
        '5 minutes': '5T',
        '5minutes': '5T',
        'five minutes': '5T',
    }

    def __init__(self, serializer_data, service_name=None):
        self.service_name = service_name
        self.interpolated_data = self.interpolation(serializer_data)

    def interpolation(self, serializer_data):
        """Interpolate data with given method in config and different timeframes"""
        df_data, config = prepare_data(serializer_data)

        try:
            df_data = df_data.resample(
                self.TIMEFRAME_TRANSLATION.get(
                    config.get('time').lower()
                )
            ).mean()
        except Exception:
            raise ValueError('config time value not recognized')

        # skip thursday and friday
        if config.get('skip_holiday'):
            df_data['time'] = df_data.index
            df_data = df_data[df_data['time'].apply(lambda x: x.weekday() not in [3, 4])]

        if config.get('interpolation') == 'linear':
            df_data['vol'] = df_data['vol'].interpolate(method='linear')
        elif config.get('interpolation') == 'spline':
            df_data['vol'] = df_data['vol'].interpolate(method='polynomial', order=2)
        else:
            raise ValueError('method not supported')

        return self.to_dictionary(df_data, config)

    def to_dictionary(self, df_data, config):
        """Convert DataFrame to python dict"""
        df_data['index'] = range(len(df_data))
        df_data['time'] = df_data.index
        df_data.index = df_data['index']
        del df_data['index']
        logging.critical(self.service_name)
        if config.get('type') == 'shamsi' or self.service_name == 'service2':
            to_jalali(df_data)

        return df_data.to_dict()
