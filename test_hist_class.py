import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inspect
from histogram import Hist

# read in data for testing from 'test_data_1.csv'
# file has 1 column of data with heading called 'col_1'
# save to pandas dataframe 'df_1'
df_1 = pd.read_csv(r'C:\projects_learning\ringvision\pypi_packages\exploratory_data_analysis\test_data_1.csv')
df_1.head(1)

def test_constructor():
    # is hist_class an 'instance' of Hist()
    hist_class = Hist(df_1,'col_1','Title Regular Hist','Bins_1','Count_y')
    assert isinstance(hist_class, Hist)

def test_class():
    # is Hist() a class
    assert inspect.isclass(Hist)

def create_object():
    # create an instance 'object' from the class Hist() 
    # will return picture of file
    test_hist_1 = Hist(df_1,'col_1','Title Regular Hist','Bins_1','Count_y')
    assert test_hist_1





# read in data for testing 'test_data_1.csv'
# file has 2 columns of data
# headings 'col_1' and 'col_2' save to pandas dataframe 'df_2'
df_2 = pd.read_csv(r'C:\projects_learning\ringvision\pypi_packages\exploratory_data_analysis\test_data_2.csv')
df_2.head(1)