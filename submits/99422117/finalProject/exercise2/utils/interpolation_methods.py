import json

import numpy as np
import pandas as pd

def gregorian_to_jalali(gy, gm, gd):
 g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
 if (gm > 2):
  gy2 = gy + 1
 else:
  gy2 = gy
 days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
 jy = -1595 + (33 * (days // 12053))
 days %= 12053
 jy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  jy += (days - 1) // 365
  days = (days - 1) % 365
 if (days < 186):
  jm = 1 + (days // 31)
  jd = 1 + (days % 31)
 else:
  jm = 7 + ((days - 186) // 30)
  jd = 1 + ((days - 186) % 30)
 return [jy, jm, jd]

def jalali_to_gregorian(jy, jm, jd):
 jy += 1595
 days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd
 if (jm < 7):
  days += (jm - 1) * 31
 else:
  days += ((jm - 7) * 30) + 186
 gy = 400 * (days // 146097)
 days %= 146097
 if (days > 36524):
  days -= 1
  gy += 100 * (days // 36524)
  days %= 36524
  if (days >= 365):
   days += 1
 gy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  gy += ((days - 1) // 365)
  days = (days - 1) % 365
 gd = days + 1
 if ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
  kab = 29
 else:
  kab = 28
 sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 gm = 0
 while (gm < 13 and gd > sal_a[gm]):
  gd -= sal_a[gm]
  gm += 1
 return [gy, gm, gd]

def linear_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='M')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='D')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='h')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='m')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    else:
        data = None

    data.set_index('time')
    return data


def spline_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='M')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='D')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='h')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='m')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    else:
        data = None

    return data


def pad_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='M')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='D')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='h')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='m')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    else:
        data = None

    return data


def nearest_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='M')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='D')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='h')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        datearray = np.datetime_as_string(data.time, unit='m')
        datelist = []
        # for idx, x in np.ndenumerate(datearray):
        #     year, month, day = x.split('-')
        #     resultarray = gregorian_to_jalali(int(year), int(month), int(day))
        #     joined = str(resultarray[0]) + '-' + str(resultarray[1]) + '-' + str(resultarray[2])
        #     datelist.append(joined)
        data.time = datearray

    else:
        data = None

    return data