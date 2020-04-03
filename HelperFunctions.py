import numpy as np


def scale_convert(self,list_to_convert):
    """Takes a list of values and scales using NumPy
    log10() and rounds two decimal places.
    
    Arguments:
        list_to_convert {list} -- List of values int or float
    
    Returns:
        list -- List of float values two decimal places
        with NumPy log10 function.
    """
    converted = np.array(list_to_convert)
    converted_ln = np.log10(converted)
    converted_ln = [round(i,2) for i in converted_ln]
    return converted_ln

def convert_thousands(self,values_to_convert, to_convert = bool):
    """Takes two inputs and divides a list of numbers by 1000
    
    Arguments:
        values_to_convert {list} -- List of values int or float
    
    Keyword Arguments:
        to_convert {bool} -- True/False if list should be converted
        (default: {True})
    
    Returns:
        [list] -- List of int values
    """
    if to_convert == True:
        convert = np.array(values_to_convert)
        converted = convert / 1000
        # returns list of int values 
        converted_values = [int(i) for i in converted]
        return converted_values 
    else:
        return values_to_convert