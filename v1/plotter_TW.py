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

      ValueError
        If the configuration file contains wrong data.

      """
      self._logger = logging.getLogger(self.__class__.__name__)
      if not type(inputFile) is str:
        self._logger.error('Name of Input file must be string')
        raise TypeError
      else:
        self.inputFile = inputFile

      try:
        with open(inputFile) as inpf:
          try:
            self.data = np.array(json.load(inpf)['presentation'])
          except:
            self._logger.error('File contains bad data')
            raise ValueError
      except IOError:
        self._logger.error('Input file not found')
        raise IOError

  def readXYData(self,dat):
      with open(dat['content']) as inpf:
            line = [i.strip() for i in inpf if i]
            xy_data = re.finditer(r'(?:[+-]?\d+\.?\d*)',line[0])
            x = []
            y= []
            for n,xy in enumerate(xy_data,1):
              if n%2 == 1:
                x.append(xy.group(0))
              if n%2 == 0:
                y.append(xy.group(0))
      return (x,y)
  


  def generatePlot(self,figName):
      """Generate a plot and save as an image.
      
      Read the data from the input file. Create a plot by using the given labels. Save the plot as an image. Return the name of the image file. 
      Parameters
      ----------
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
      for dat in self.data:
        if dat['type'] == 'plot':
          self.x,self.y = self.readXYData(dat)
          self.fig,self.ax = plt.subplots()
          self.ax.plot(self.x,self.y)
          self.ax.set_xlabel(dat['configuration']['x-label'])
          self.ax.set_ylabel(dat['configuration']['y-label'])
          self.ax.set_title(dat['title'])
          self.fig.savefig(figName)

if __name__ == "__main__":
    plotter = Plotter('sample.json')
    plotter.generatePlot('figname.png')