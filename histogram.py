import matplotlib.pyplot as plt
import numpy as np
from EDAVisual import OptionsHist
from HelperFunctions import scale_convert, convert_thousands

       
class Hist(OptionsHist):
    """Predefined histogram with basic settings to quickly plot data
    
    Arguments:
        OptionsHist {class} -- Settings from parent class
    """
    def __init__(self, dataframe, col_name, title, x_name, y_name):
        """Predefined histogram configurations from parent class 
        EDAVisual.OptionsHist 
    
        Arguments:
            dataframe {pandas.DataFrame} -- DataFrame containing columns 
            col_name {pandas.Series} -- str name of column from pandas dataframe
            title {str} -- str name of chart title
            x_name {str} -- str name of x-axis 
            y_name {str} -- str name of y-axis
            xticks {int} -- fontsize (14) setting of values on x-axis
            yticks {int} -- fontsize (14) setting of values on y-axis
        """

        OptionsHist.__init__(self, dataframe, col_name, title, x_name, y_name)
        
        self.mu_line = plt.axvline(np.mean(dataframe[col_name]), color='r',
                                  linestyle = '--', lw=2, label = 'Mean')
        self.med_line = plt.axvline(np.median(dataframe[col_name]), color = 'y',
                                  linestyle='--', lw = 2, label = 'Median')
        plt.legend(fontsize=14)
        plt.hist(dataframe[col_name]);
        

class HistBins(OptionsHist):
    """Predefined histogram that adjusts the bin size to improve view.
    
    Arguments:
        OptionsHist {class} -- Settings from parent class
    """ 
    def __init__(self, dataframe, col_name, title, x_name, y_name , start, 
                 stop, bin_size):
        """Predefined histogram that adjusts the bin size to improve view
        
        Arguments:
        dataframe {pandas.DataFrame} -- DataFrame containing columns 
        col_name {pandas.Series} -- str name of column from pandas dataframe
        title {str} -- str name of chart title
        x_name {str} -- str name of x-axis 
        y_name {str} -- str name of y-axis
        xticks {int} -- fontsize (14) setting of values on x-axis
        yticks {int} -- fontsize (14) setting of values on y-axis
        start {int} -- starting value of bin range 
        stop {int} -- ending value of bin range
        bin_size {int} -- the size of each individual bin
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
        plt.hist(dataframe[col_name], bins = self.bin_edges);
        


class HistLog10(OptionsHist):
    """Histogram of scaled data using log base 10 or with the x-axis values
    non-scaled or converted to thousands.
    
    Arguments:
        OptionsHist {class} -- Settings from parent class
    """
    def __init__(self, dataframe, col_name, title, x_name, y_name, x_axis_scale,
                 start, bin_size, thousands = bool):
        """[summary]
        
        Arguments:
        dataframe {pandas.DataFrame} -- DataFrame containing columns 
        col_name {pandas.Series} -- str name of column from pandas dataframe
        title {str} -- str name of chart title
        x_name {str} -- str name of x-axis 
        y_name {str} -- str name of y-axis
        xticks {int} -- fontsize (14) setting of values on x-axis
        yticks {int} -- fontsize (14) setting of values on y-axis
        x_axis_scale {list} -- list of values provided by user to show x-axis label values
        which is in-place of the logarithmic scale
        start {int} -- starting value of bin range 
        bin_size {int} -- the size of each individual bin

        Keyword Arguments:
            thousands {bool} -- True/False if x-axis label values are divided
            by 1000. This is the x_axis_scale (default: {True})
        """
        OptionsHist.__init__(self, dataframe, col_name, title, x_name, y_name)
        
        # list of values provided by user to show as x-axis label values
        # which is in-place of the logarithmic scale
        self.x_axis_scale = x_axis_scale 
        self.start = start
        self.bin_size = bin_size
        # determine if non logarithmic x-axis label values should divided by 1000
        self.thousands = thousands
        self.log_data = np.log10(dataframe[col_name]) # direct data transform
        self.log_bin_edges = np.arange(self.start, self.log_data.max() + self.bin_size,
                                       self.bin_size)
        self.mu_line = plt.axvline(np.mean(self.log_data), color = 'r',
                                  linestyle = '--', lw = 2, label = 'Mean')
        
        self.median_line = plt.axvline(np.median(self.log_data), color = 'y',
                                  linestyle = '--', lw = 2, label = 'Median')
       
        # workaround to hide the minor tick labels from showing
        # if not logarithmic label values are shown 
        plt.tick_params(axis='both', which='minor', labelsize=0)
        plt.legend(fontsize=14)

        #### different options for trying to solve x-axis ### 
        # get the current x location and labels 
        locs, labels = plt.xticks()
        
        print(f"What is value thousands {thousands}")
        print(f"x_axis_labels {self.x_axis_scale}")
        print(f"Conv labels >> {convert_thousands(self.x_axis_scale, self.thousands)}")
        print(f"bin edges = {self.log_bin_edges}")
        print(locs)
        print(labels)
        # z = [1.0, 1.18, 1.3, 1.4, 1.48, 1.54, 1.6, 1.65, 1.7, 1.74, 1.78, 1.81, 1.85, 1.88]
        # t = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
        # plt.xticks(ticks = z, labels = t, fontsize = 14)

        # if true convert the x-axis label values to thousand and pass for use 
        # in plt.xticks()
        x_axis_label = convert_thousands(self.x_axis_scale, self.thousands)
        # convert the x-axis values log10. Will be used to assign location 
        # of the x-axis labels see plt.xticks()
        x_axis_log10 = scale_convert(self.x_axis_scale)

        plt.xticks(ticks = x_axis_log10, labels = x_axis_label,
                  fontsize = 25)
        
        # first plot histogram then plt.xscale() - This is required or Matpotlib will 
        # show the logarithmic scale 
        plt.hist(self.log_data, bins = self.log_bin_edges)

        # set the x-axis to log with base value of 10
        plt.xscale('log')
        plt.show();

        hist_obj_1 = Hist(df, 'score', 'Title Hist Object-1' , 'Bins', 'Counts')
        print(hist_obj_1)
        plt.show()
