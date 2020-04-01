import matplotlib.pyplot as plt
import numpy as np
from EDAVisual import OptionsHist

       
class Hist(OptionsHist):
    """[summary]
    
    Arguments:
        OptionsHist {[type]} -- [description]
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
        OptionsHist.__init__(self, dataframe, col_name, title, x_name, y_name)
        
        self.mu_line = plt.axvline(np.mean(dataframe[col_name]), color='r',
                                  linestyle = '--', lw=2, label = 'Mean')
        self.med_line = plt.axvline(np.median(dataframe[col_name]), color = 'y',
                                  linestyle='--', lw = 2, label = 'Median')
        plt.legend(fontsize=14)
        plt.hist(dataframe[col_name])    

class HistBins(OptionsHist):
    """[summary]
    
    Arguments:
        OptionsHist {[type]} -- [description]
    """ 
    def __init__(self, dataframe, col_name, title, x_name, y_name , start, 
                 stop, bin_size):
        """[summary]
        
        Arguments:
            dataframe {[type]} -- [description]
            col_name {[type]} -- [description]
            title {[type]} -- [description]
            x_name {[type]} -- [description]
            y_name {[type]} -- [description]
            start {[type]} -- [description]
            stop {[type]} -- [description]
            bin_size {[type]} -- [description]
        """
        OptionsHist.__init__(self, dataframe, col_name, title, x_name, y_name)
        self.start = start
        self.stop = stop
        self.bin_size = bin_size
        self.bin_edges = np.arange(self.start, self.stop + self.bin_size, 
                                   self.bin_size)    
        self.mu_line = plt.axvline(np.mean(dataframe[col_name]),color = 'r',
                                  linestyle = '--', lw = 2, label = 'Mean')
        self.med_line = plt.axvline(np.median(dataframe[col_name]), color = 'y',
                                  linestyle = '--', lw=2, label = 'Median')
        plt.legend(fontsize=14)
        plt.hist(dataframe[col_name], bins = self.bin_edges)    


class HistLog10(OptionsHist):
    """Create a histogram with logarithmic scale (log10).
    Arguments:
        OptionsHist {[type]} -- [description]
    """
    def __init__(self, dataframe, col_name, title, x_name, y_name, x_axis_scale,
                 start, bin_size, thousands = bool):
        """[summary]
        
        Arguments:
            dataframe {[type]} -- [description]
            col_name {[type]} -- [description]
            title {[type]} -- [description]
            x_name {[type]} -- [description]
            y_name {[type]} -- [description]
            x_axis_scale {[type]} -- [description]
            start {[type]} -- [description]
            bin_size {[type]} -- [description]
        
        Keyword Arguments:
            thousands {[type]} -- [description] (default: {bool})
        """
        OptionsHist.__init__(self, dataframe, col_name, title, x_name, y_name)

        self.start = start
        self.x_axis_scale = [] # list of values provided by user for x axis
        self.bin_size = bin_size #  will set the interval of bins
        self.log_data = np.log10(dataframe[col_name]) # direct data transform
        self.log_bin_edges = np.arange(self.start, self.log_data.max() + self.bin_size,
                                       self.bin_size)
        
        self.mu_line = plt.axvline(np.mean(self.log_data), color = 'r',
                                  linestyle = '--', lw = 2, label = 'Mean')
        
        self.median_line = plt.axvline(np.median(self.log_data), color = 'y',
                                  linestyle = '--', lw = 2, label = 'Median')
        
        self.thousands = thousands
        #self.convert_ticks = ''
        self.converted_labels = ''
        
        # FIRST plot histogram then plot x-scale and x-ticks otherwise x-axis will be logarithmic
        plt.hist(self.log_data, bins = self.log_bin_edges)
        plt.xscale('log')
        plt.tick_params(axis='both', which='minor', labelsize=0)
        plt.legend(fontsize=14);
        
        # ticks is base 10 used to set the axis. Show either base converted or non converted values
        self.xticks = plt.xticks(ticks = self.x_axis_scale, labels = self.converted_labels)

    def scale_convert(self, list_to_convert):
        """[summary]
        
        Arguments:
            list_to_convert {[type]} -- [description]
        """
        converted = np.array(list_to_convert)
        converted_ln = np.log10(converted)
        converted_ln = [round(i,2) for i in converted_ln]
        self.x_axis_scale = converted_ln

    def convert_thousands(self, list_to_convert):
        """[summary]
        
        Arguments:
            list_to_convert {[type]} -- [description]
        """
        if self.thousands == True:
            list_to_convert = np.array(list_to_convert)
            converted = list_to_convert / 1000
            converted_values = [int(i) for i in converted]
            self.convert_labels =  converted_values
