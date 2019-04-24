import logging


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
      if not isinstance(str,inputFile):
        logging.error('Name of Input file must be string')
        raise TypeError
      else:
        self.inputFile = inputFile

      try:
        with open(inputFile) as inpf:
          try:
            pass
          except:
            logging.error('File contains bad data')
            raise ValueError
      except IOError:
        logging.error('Input file not found')
        raise IOError



  def generatePlot(self,xLabel,yLabel):
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
    

if __name__ == "__main__":

