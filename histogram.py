import matplotlib.pyplot as plt
import numpy as np
from EDA_visual import OptionsHist

class Hist(OptionsHist):
    def __init__(self, dataframe, col_name, x_name, 
                 y_name):
        OptionsHist.__init__(self, dataframe, col_name, x_name, 
                 y_name)
        plt.hist(dataframe[col_name])


class HistBins(OptionsHist):
    def __init__(self, dataframe, col_name, x_name, 
                 y_name,start, stop, binsize):
        OptionsHist.__init__(self, dataframe, col_name, x_name, 
                 y_name)
        self.start = start
        self.stop = stop
        self.binsize = binsize
        self.bin_edges = np.arange(self.start, self.stop + self.binsize, self.binsize)    
        plt.hist(dataframe[col_name], bins = self.bin_edges)

class HistLog10(OptionsHist):
    """Create a histogram with logarithmic scale (log10).
    Arguments:
        OptionsHist {[type]} -- [description]
    """
    def __init__(self, dataframe, col_name, x_name, y_name, start,
                x_axis_scale, binsize, thousands = bool):
        OptionsHist.__init__(self, dataframe, col_name, x_name, 
                 y_name)
        
        self.start = start
        self.x_axis_scale = [] # list of values provided by user for x axis
        self.binsize = binsize #  will set the interval of bins
        self.log_data = np.log10(dataframe[col_name]) # direct data transform
        self.log_bin_edges = np.arange(self.start, self.log_data.max() + self.binsize, self.binsize)
        self.mu_line = plt.axvline(np.mean(self.log_data),color='r',
                                  linestyle='--',lw=2,label='Mean')
        self.median_line = plt.axvline(np.median(self.log_data),color='y',
                                  linestyle='--',lw=2,label='Median')
        self.thousands = thousands
        self.convert_ticks = ''
        self.converted_labels = ''

        # ticks is base 10 used to set the axis. Show either base converted or non converted values
        self.xticks = plt.xticks(ticks = self.x_axis_scale, labels = self.converted_labels)

    def scale_convert(self,list_to_convert):
        """Convert list of values using NumPy log10(). 
        Arguments:
            list_to_convert {list} -- A list of values used for x or y axis for use
            when pandas data has been transformed. 
        Returns:
            [numpy list] -- A list of converted values using Numpy log10.
        """
        converted = np.array(list_to_convert)
        converted_ln = np.log10(converted)
        converted_ln = [round(i,2) for i in converted_ln]
        self.x_axis_scale = converted_ln

    def convert_thousands(self, list_to_convert):
        """Convert the x axis scale to thousands. Convert if bool thousands is True.

        Arguments:
            list_to_convert {list} -- The list of values to be converted to thousands
        Returns:
            [list] -- Will return a list that will be converted or not based self.thousands bool
        """
        if self.thousands == True:
            list_to_convert = np.array(list_to_convert)
            converted = list_to_convert / 1000
            converted_values = [int(i) for i in converted]
            self.convert_labels =  converted_values 

        # FIRST plot histogram then plot xscale and xticks otherwise x-axis will be logarithmic
        plt.hist(self.log_data, bins = self.log_bin_edges)
        plt.xscale('log')
        plt.tick_params(axis='both', which='minor', labelsize=0);
        
        