import matplotlib.pyplot as plt
import numpy as np

class OptionsHist():
    """The parent to histogram.py which allows users to quickly create standard
    histograms during initial data analysis process.
    """

    def __init__(self, dataframe, col_name, title, x_name, y_name):
    """[summary]
    
    Arguments:
        dataframe {[type]} -- [description]
        col_name {[type]} -- [description]
        title {[type]} -- [description]
        x_name {[type]} -- [description]
        y_name {[type]} -- [description]
    """
        self.dataframe = dataframe
        self.col_name = col_name
        self.x_name = plt.xlabel(x_name,fontsize=14)
        self.y_name = plt.ylabel(y_name,fontsize=14)
        self.title = plt.title(title,fontsize=14)
        self.xticks = plt.xticks(fontsize=14)
        self.yticks = plt.yticks(fontsize=14)
         
