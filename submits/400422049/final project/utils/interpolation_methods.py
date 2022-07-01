from scipy import *
from flask import abort , make_response

def linear_interpolation(data, config):
    
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M').last()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
    
    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D').last()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('H').last()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('min').last()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def spline_interpolation(data,config) :
    spline_Exception_string = "there's something wrong with the number of control points in your records to do spline interpolation!"
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M').last()
        
        try:
            data = data.interpolate(method=config['interpolation'], order=3)
        except:
            abort(make_response(spline_Exception_string))
        
        data.reset_index(inplace=True)
    

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D').last()
        
        try:
            data = data.interpolate(method=config['interpolation'], order=3)
        except:
            abort(make_response(spline_Exception_string))
        
        data.reset_index(inplace=True)


    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('H').last()
        
        try:
            data = data.interpolate(method=config['interpolation'], order=3)
        except:
            abort(make_response(spline_Exception_string))
        
        data.reset_index(inplace=True)


    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('min').last()
        
        try:
            data = data.interpolate(method=config['interpolation'], order=3)
        except:
            abort(make_response(spline_Exception_string))
        
        data.reset_index(inplace=True)


    else:
        data = None

    return data
