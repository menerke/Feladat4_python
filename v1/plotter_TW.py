import logging
import numpy as np
import json
import matplotlib.pyplot as plt
import re


class Plotter:
    def __init__(self,inputFile):
        """Initialization.

        Set up the logger. Store the name of the input file.
        Parameters
        ----------
        inputFile : str
            The name of the input file. It contains the data to be plotted.

        Raises
        ----------
        TypeError
            If the inputFile is not a string.

        IOError
            If the file can not be read. 
        """
        self._logger = logging.getLogger(self.__class__.__name__)

        if not type(inputFile) is str:
             self._logger.error('Name of Input file must be string')
             raise TypeError
        else:
            self.inputFile = inputFile
        try:
            with open(inputFile) as inpf:
                pass
        except:
            self._logger.error('Input file not found')
            raise IOError
    
    def readXYData(self,inputFile):
        """Read the x,y data sets.
        
        Read the data from the input file. Return a tuple which contains the x,y data.
        Parameters
        ----------
        inputFile : str
            The name of the input file. It contains the data to be plotted.

        Returns
        -------
        x,y
            A tuple contains the x,y data.
        """
        with open(inputFile) as inpf:
                    line = [i.strip() for i in inpf if i]
                    xy_data = re.finditer(r'(?:[+-]?\d+\.?\d*)',line[0])
                    x = []
                    y= []
                    for n,xy in enumerate(xy_data,1):
                        if n%2 == 1:
                            x.append(float(xy.group(0)))
                        if n%2 == 0:
                            y.append(float(xy.group(0)))
        return (x,y)

    def generatePlot(self,inputFile,xLabel,yLabel):
        """Generate a plot and save as an image.
        
        Read the data from the input file by using an another function. Create a plot by using the given labels. Save the plot as an image. Return the name of the image file. 
        Parameters
        ----------
        inputFile : str
            The name of the input file. It contains the data to be plotted.
        xLabel : str
            The label of the x axis.
        yLabel : str
            The label of the y axis.

        Returns
        -------
        str
            The filename of the image file.

        Raises
        ----------
        TypeError
            If the xLabel or yLabel is not a string.

        IOError
            If the image file can not be written. 
        """

        if not type(xLabel) or not type(yLabel) is str:
            self._logger.error('The labels must be strings.')
            raise TypeError

        plotter = Plotter(inputFile)
        data = plotter.readXYData(inputFile)
        x = np.array(data[0])
        y = np.array(data[1])
        fig,ax = plt.subplots()
        ax.plot(x,y)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        figName = 'figure.png'
        try:
            fig.savefig(figName)
        except:
            self._logger.error('The figure can not be written.')
            raise IOError
        return figName