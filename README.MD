***
# Exploratory Data Analysis Tools
***


***
# Description 
***

This package is a set of commonly used tools for the Exploratory Data Analysis `EDA` process. They allow the user to quickly produce more detailed visual plots or functions for analysis. The first release will have four modules with three (3) different histograms that can be used during the EDA process.  

***
# Modules 
***


## EDAVisual

EDA_visual is the generic file for creating individual visualization classes. This module will contain the base class each of main types of charts that can be generated. The first release will have one base class called `OptionsHist`. 
  

## HelpFunctions

This module contains helper functions used within the other modules.  The first release contains two (2) functions:
1. `scale_convert` - Takes a list of values scales the values using the NumPy function `log10()`  and rounds the values to two decimal places. 
2. `convert_thousands` - Reads a bool value and if True converts a provided list of values into thousands (000'). Typically this will be the label values for the x-values making it easier read.  


## histogram 

Module containing three (3) histograms that allow user to create three different types of histograms.
1. Basic histogram with mean and median line plotted
2. Histogram with ability to quickly adjust the bins
3. Histogram with prior functionality, data transformed to logarithmic scale and x-axis labels with non logarithmic values with option to convert to thousands. 

***
# Testing 
***
For testing we used `pytest`. 

## test_help_func


## test_hist


***
# Authors 
***

Brian Ringler 

***
# License
***

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details