import logging
import json

from presentation_generator_TW import PresentationGenerator
from plotter_TW import Plotter

class Presentation:
    """The main class to create the pptx. One function (generate) should go through the configuration (JSON) file, and call the appropriate module/object/function. 
    The output is the generated pptx file."""

    def __init__(self,outputFileName,templateFileName):
        """Initialization.

        Set up the logger. Call the generator module with the name of the output file.
        Parameters
        ----------
        outputFileName : str
            The name of the output pptx file.            
        templateFileName : str
            The name of the template file. 
        Raises
        ----------
        TypeError
            If the outputFileName is not a string.
        """
        self._logger = logging.getLogger(self.__class__.__name__)
        self._generator = PresentationGenerator(outputFileName,templateFileName)

    def layoutSelect(self,stype):
        """Select the layout of the slide.

        According to the stype of the slide, the function returns with a number to select the layout. The template presentation must be known.    

        Parameters
        ----------
        stype : str
            The stype of the slide. 

        Returns
        -------
        layoutNumber : int
            The number of the appropriate layout. 
        
        Raises
        ----------
        TypeError
            If the stype is not a string.

        ValueError
            If the stype is not appropriate.
        """
        if not type(stype) is str:
            self._logger.error('The slide type must be string.')
            raise TypeError

        if stype == 'title':
            return 0
        elif stype == 'list':
            return 1
        elif stype == 'picture':
            return 5
        elif stype == 'plot':
            return 5
        elif stype == 'text':
            return 5
        else:
            self._logger.error('There is an inaproppriate slide type.')
            raise ValueError

    def generate(self,configFileName):
        """Read the configuration (JSON) file and act accordingly.
        
        The configuration file should contain the type of the slide. The generate function calls the appropriate functions accordind to the different types. 
        The configuration file usually contains every information needed to generate the slide, except the layout number. 
        The layout number should be chosen according to the type of the slide by using the layoutSelect. The layout number is an input for every function of the presentation generator.     
        But there are cases, when other opreations must be done before calling the slide generator. 
        In case of the Plot slide, first, the Plotter module should be called and the image file should be generated. 
        In case of the List slide, a numpy array containing the levels and the numpy array containing the lines should be generated. 
        (There is no need to do the conversion with an other function.) 

        Parameters
        ----------
        configFileName : str
            The name of the configuration (JSON) file.            
        
        Returns
        -------
        bool
            True if the pptx generation is successful, False otherwise.

        Raises
        ----------
        TypeError
            If the outputFileName is not a string.

        IOError
            If the config file can not be read. If the pptx file can not be written.

        ValueError
            If the configuration file contains wrong data.

        """
        try:
            with open(configFileName) as inpf:
                try:
                    self.data = json.load(inpf)['presentation']
                except:
                    self._logger.error('File contains bad data')
                    raise ValueError
        except IOError:
            self._logger.error('Input file not found')
            raise IOError
        
        for dat in self.data:
            if dat['type'] == 'text':
                self._generator.addText(presentation.layoutSelect(dat['type']),dat['title'],dat['content'])
            elif dat['type'] == 'title':
                self._generator.addTitle(presentation.layoutSelect(dat['type']),dat['title'],dat['content'])
            elif dat['type'] == 'list':
                levels = []
                text = []
                for level in dat['content']:
                    levels.append(level['level'])
                    text.append(level['text'])
                self._generator.addList(presentation.layoutSelect(dat['type']),dat['title'],levels,text)
            elif dat['type'] == 'picture':
                self._generator.addImage(presentation.layoutSelect(dat['type']),dat['title'],dat['content'])
            elif dat['type'] == 'plot':
                plotImage = Plotter(dat['content']).generatePlot(dat['content'],dat['configuration']['x-label'],dat['configuration']['y-label'])
                self._generator.addPlot(presentation.layoutSelect(dat['type']),dat['title'],plotImage)
        self._generator.finalize()

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level = logging.INFO)
    presentation = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
    presentation.generate("sample.json")
