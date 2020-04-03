import matplotlib.pyplot as plt

class OptionsHist():
    """The parent class to pre-constructed Matplotlib histograms"""

    def __init__(self, dataframe, col_name, title, x_name, y_name):
        """Predefined histogram configurations. 
        
        Arguments:
            dataframe {pandas.DataFrame} -- DataFrame containing columns 
            col_name {pandas.Series} -- str name of column from pandas dataframe
            title {str} -- str name of chart title
            x_name {str} -- str name of x-axis 
            y_name {str} -- str name of y-axis
            xticks {int} -- fontsize (14) setting of values on x-axis
            yticks {int} -- fontsize (14) setting of values on y-axis
        """
        self.dataframe = dataframe
        self.col_name = col_name
        self.x_name = plt.xlabel(x_name,fontsize=14)
        self.y_name = plt.ylabel(y_name,fontsize=14)
        self.title = plt.title(title,fontsize=14)
        self.xticks = plt.xticks(fontsize=14)
        self.yticks = plt.yticks(fontsize=14) 
         
