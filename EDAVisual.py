import matplotlib.pyplot as plt
import numpy as np

class OptionsHist():
    """The parent to histogram.py which allows users to quickly create standard
    histograms during initial data analysis process.
    """
    
    def __init__(self, dataframe, col_name, x_name, 
                 y_name):
        """[summary]
        
        Arguments:
            dataframe {pd.DataFrame} -- Pandas dataframe can be more than one feature
            col_name {pd.Series} -- Pandas series that will be plotted
            x_name {str} -- The label for the x axis 
            y_name {str} -- The label for the y axis
        """
        self.dataframe = dataframe
        self.col_name = col_name
        self.x_name = plt.xlabel(x_name,fontsize=14)
        self.y_name = plt.ylabel(y_name,fontsize=14)
        self.bins = ''
        self.mu_line = plt.axvline(np.mean(dataframe[col_name]),color='r',
                                  linestyle='--',lw=2,label='Mean')
        self.median_line = plt.axvline(np.median(dataframe[col_name]),color='y',
                                  linestyle='--',lw=2,label='Median')
        self.xticks = plt.xticks(fontsize=14)
        self.yticks = plt.yticks(fontsize=14)
        self.title = plt.title(fontsize=14)
        self.legend = plt.legend(fontsize=14) 
         