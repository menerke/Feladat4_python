import logging

from presentation_generator_TW import PresentationGenerator
from presentation_formatter import PresentationFormatter

class Presentation:
    """The main class to create the pptx. One function (generate) should go through the configuration (JSON) file, and call the appropriate module/object/function. 
    The output is the generated pptx file."""

    def __init__(self,outputFileName):
        """Initialization.

        Set up the logger. Call the generator module with the name of the output file.
        Parameters
        ----------
        outputFileName : str
            The name of the output pptx file.            

        Raises
        ----------
        TypeError
            If the outputFileName is not a string.

        """
        #self._generator = PresentationGenerator('PYTHON-Environment.pptx')
        #self._formatter = PresentationFormatter()

    def layoutSelect(self,type):
        """Select the layout of the slide.

        According to the type of the slide, the function returns with a number to select the layout. The template presentation must be known.    

        Parameters
        ----------
        type : str
            The type of the slide. 

        Returns
        -------
        layoutNumber : int
            The number of the appropriate layout. 
        
        Raises
        ----------
        TypeError
            If the type is not a string.

        ValueError
            If the type is not appropriate.
        """

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
        presentationGenerator = PresentationGenerator('outputFileName')
        try:
            with open(configFileName) as inpf:
                try:
                    self.data = np.array(json.load(inpf)['presentation'])
                except:
                    self._logger.error('File contains bad data')
                    raise ValueError
        except IOError:
            self._logger.error('Input file not found')
            raise IOError
        
        for dat in self.data:
            if dat['type'] == 'plot':
                plotter = Plotter(dat)
                figName = plotter.generatePlot('figure.png')

        #self._generator.addTitle("PYTHON oktatás", "Kaszás Gábor")
        
        #self._generator.addList("Fejlesztői környezet", "Szükséges szoftverek", 
        #    [[1, "PYTHON v3.7.2"],
        #     [2, "https://www.python.org/downloads/"],
        #     [2, "https://www.python.org/downloads/release/python-372/"],
        #     [1, "Visual Studio Code V.1.31.1 (legfrissebb)"],
        #     [2, "https://code.visualstudio.com/"],
        #     [1, "GIT v2.20.1 (legfrissebb)"],
        #     [2, "https://git-scm.com/download/win"],
        #     ])

if __name__ == "__main__":
    pass
    #logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level = logging.INFO)
    #presentation = Presentation()
    #presentation.generate()
