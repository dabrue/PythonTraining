#!/bin/env python3
"""
    This script reads the data generated by genData.py and makes a plot
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

if (__name__ == "__main__"):
    
    # The plotting routines are provided by matplotlib. The basic plotting facility
    # is the pyplot module. Note that imported modules can be renamed.
    import matplotlib.pyplot as plt

    # define empty lists for storing the data
    x,y0,y1,y2 = [],[],[],[]

    # open the data file in reading mode
    inf = open("simpledata.dat","r")

    for line in inf:  # File objects are iterable! 
        
        # remove the new line. Not necessary in this case, but good practice
        # the rstrip string method does not "change in place". 
        line=line.rstrip("\n")  

        # split the line into fields
        data = line.split() 

        # data is now a list containing the fields. Time for sanity check. 
        if (len(data) < 2):
            print("ERROR: Unexpected number of fields")
            exit(2)   # the argument of the exit() command is the returned error code

        # populate lists
        x.append(float(data[0]))
        y0.append(float(data[1]))
        y1.append(float(data[2]))
        y2.append(float(data[3]))

    # note that we're now out of the for loop. Close the file. 
    inf.close()

    # PLOT 1: really simple plotting
    plt.plot(x,y0)
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.show()


    # PLOT 2: a little more detail. 
    fig = plt.figure()   # create a figure object. This is implicitly done in PLOT1

    # Next we use the add_subplot method to generate subplots in the figure. This 
    # figure will have 3 plots. The arguments to add_subplot describe how 
    # the subplots are arranged, (nrows, ncols, plotnumber). Here we'll make a figure
    # with three subplots in a column, so three rows....
    ax0=fig.add_subplot(3,1,1)  # Create first subplot
    plt.plot(x,y0)
    ax1=fig.add_subplot(3,1,2)
    plt.plot(x,y1)
    ax2=fig.add_subplot(3,1,3)
    plt.plot(x,y2)

    # Nothing happens without a plot.show or plot.save
    #plt.show()
