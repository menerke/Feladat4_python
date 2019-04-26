import logging

from pptx import Presentation
from pptx.util import Inches
from pptx.util import Cm

from presentation_io import PresentationIO

class PresentationGenerator:
    """The generator class.

    It creates different type of slides. The available types: Title, Text, Image, List, Plot.
    """

    def __init__(self, outputFileName):
        """Initialization.
        
        Set up the logger. Give the template file of the presentation.

        Parameters
        ----------
        outputFileName : str
            The name of the output file.

        Raises
        ----------
        TypeError
            If the outputFileName is not a string.

        IOError
            If the file can not be written. 

        ValueError
            If the outputFileName has not .pptx extension.
        
        """
        self._logger = logging.getLogger(self.__class__.__name__)
        if not type(outputFileName) is str:
            self._logger.error('Name of Output file must be string')
            raise TypeError
        else:
            if outputFileName.endswith('.pptx'):
                self._outputFileName = outputFileName
            else:
                raise ValueError

        """
        EZ a rész bizonytalan, nem látom az IOError milyen fájl írást ellenőrizzen, nem elég ez a "    def finalize(self):"-ben?
        try:
            VALAMI
        except IOError as e:
            self._logger.error("I/O error({0}): {1}".format(e.errno, e.strerror))    
        """

        self._presentation = Presentation(self._outputFileName)

        #self._logger = logging.getLogger(self.__class__.__name__)
        #self._io = PresentationIO()
        #self._presentation = Presentation("PYTHON-Course.template")
        #self._fileName = fileName

    def addTitle(self, layout, title, subTitle):
        """Generate the Title slide. 

        The slide contains the title and the subtitle. The function should select the layout first, then add a new slide and write the title and subtitle text.
        
        Parameters
        ----------
        layout : int
            The number of the layout to be selected. 
        title : str
            The string contains the title text. 
        subTitle : str
            The string contains the subtitle text. 

        Returns
        -------
        bool
            True if the slide generation is successful, False otherwise.

        Raises
        ----------
        SystemError
            If the slide generation is not successful. 
        """
        slideLayout = self._presentation.slide_layouts[layout]
        try:
            slide = self._presentation.slides.add_slide(slideLayout)
            slide.shapes.title.text = title
            slide.placeholders[1].text = subTitle
            self._logger.info("Title page is added ({0}, {1})".format(title, subTitle))
            return True
        except:
            raise SystemError
            return False
        #titleSlideLayout = self._presentation.slide_layouts[0]
        #slide = self._presentation.slides.add_slide(titleSlideLayout)
        #titleShape = slide.shapes.title
        #subTitleShape = slide.placeholders[1]
        #titleShape.text = title
        #subTitleShape.text = subTitle
        #self._logger.info("Title page is added ({0}, {1})".format(title, subTitle))

    def addText(self, layout, title, text):
        """Generate the Text slide. 
        
        The slide contains a title and a longer text. It should select the layout first, then add a new slide and write the title and the long text.
        
        Parameters
        ----------
        layout : int
            The number of the layout to be selected. 
        title : str
            The string contains the title text. 
        text : str
            The string contains the long text. 

        Returns
        -------
        bool
            True if the slide generation is successful, False otherwise.

        Raises
        ----------
        SystemError
            If the slide generation is not successful. 
        
        """
        slideLayout = self._presentation.slide_layouts[layout]
        try:
            slide = self._presentation.slides.add_slide(slideLayout)
            slide.shapes.title.text = title
            slide.placeholders[1].text = text
            left = Cm(3.5)
            top = Cm(3.0)
            height = Cm(14.5)
            width = Cm(30.0)
            textBox = slide.shapes.add_textbox(left, top, height, width)
            textBox.text_frame.text = text
            self._logger.info("Title page is added ({0}, {1})".format(title, text))
            return True
        except:
            raise SystemError
            return False


        #titleOnlySlideLayout = self._presentation.slide_layouts[5]
        #slide = self._presentation.slides.add_slide(titleOnlySlideLayout)
        #titleShape = slide.shapes.title
        #titleShape.text = title
        #left = Cm(3.5)
        #top = Cm(3.0)
        #height = Cm(14.5)
        #width = Cm(30.0)
        #textBox = slide.shapes.add_textbox(left, top, height, width)
        #textFrame = textBox.text_frame
        #textFrame.text = text

    def addList(self, layout, title, levels, text):
        """Generate the List slide. 
        
        The slide contains a title and a list. The number of the level is also an input. 
        It should select the layout first, then add a new slide and write the title and the text on the appropriate level.
        
        Parameters
        ----------
        layout : int
            The number of the layout to be selected. 
        title : str
            The string contains the title text. 
        levels: numpy array
            The numpy array contains the numbers to select the level of the list. 
        text : numpy array
            The numpy array contains the the text line by line (as a string). 

        Returns
        -------
        bool
            True if the slide generation is successful, False otherwise.

        Raises
        ----------
        SystemError
            If the slide generation is not successful. 
        
        """
        #bulletSlideLayout = self._presentation.slide_layouts[1]
        #slide = self._presentation.slides.add_slide(bulletSlideLayout)
        #shapes = slide.shapes
        #titleShape = shapes.title
        #bodyShape = shapes.placeholders[1]
        #titleShape.text = title
        #textFrame = bodyShape.text_frame
        #textFrame.text = text
        #for line in lines:
        #    paragraph = textFrame.add_paragraph()
        #    paragraph.level = line[0]
        #    paragraph.text = line[1]
    
    def addImage(self, layout, title, fileName):
            """Generate the Image slide. 
            
            The slide contains a title and an image. It should select the layout first, then add a new slide and write the title and add the image.
            
            Parameters
            ----------
            layout : int
                The number of the layout to be selected. 
            title : str
                The string contains the title text. 
            fileName: str
                The name of the image file.

            Returns
            -------
            bool
                True if the slide generation is successful, False otherwise.

            Raises
            ----------
            SystemError
                If the slide generation is not successful. 
         
            """
        #titleOnlySlideLayout = self._presentation.slide_layouts[5]
        #slide = self._presentation.slides.add_slide(titleOnlySlideLayout)
        #titleShape = slide.shapes.title
        #titleShape.text = title
        #left = Cm(3.5)
        #top = Cm(3.0)
        #picture = slide.shapes.add_picture(fileName, left, top)
        #self._logger.info("Image page is added ({0}, {1})".format(title, fileName))

    def addPlot(self, layout, title, plotName):
        """Generate the Plot slide. 
        
        The slide contains a title and an image named plotName. It should select the layout first, then add a new slide and write the title and add the image.
                    
        Parameters
        ----------
        layout : int
            The number of the layout to be selected. 
        title : str
            The string contains the title text. 
        plotName: str
            The name of the image file.

        Returns
        -------
        bool
            True if the slide generation is successful, False otherwise.

        Raises
        ----------
        SystemError
            If the slide generation is not successful. 

        """
        #titleOnlySlideLayout = self._presentation.slide_layouts[5]
        #slide = self._presentation.slides.add_slide(titleOnlySlideLayout)
        #titleShape = slide.shapes.title
        #titleShape.text = title
        #left = Cm(3.5)
        #top = Cm(3.0)
        #picture = slide.shapes.add_picture(plotName, left, top)
        #self._logger.info("Image page is added ({0}, {1})".format(title, plotName))

    def finalize(self):
        """Save the created pptx.
    
        Returns
        -------
        bool
            True if the slide generation is successful, False otherwise.

        Raises
        ----------
        IOError
            If the finalization is not successfull, so the pptx file can not be written. 

        """
        try:
            self._presentation.save(self._outputFileName)
            return True
        except:
            raise IOError
            return False
        #self._presentation.save(self._fileName)
        #self._logger.info("Presentation is closed ({0})".format(self._fileName))

if __name__ == "__main__":
    pass
    # logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(filename)s(%(lineno)s) %(message)s", level = logging.INFO)
    #logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level = logging.INFO)
    #generator = PresentationGenerator('PYTHON-Course-1.pptx')
    #generator.addTitle("PYTHON Course", "Created by Gábor Kaszás")
    #generator.addText("Sample Text", generator._io.loadTextFile("presentation/presentation_io.py")[0:200])
    #generator.addImage("Sample Code", "presentation_formatter.png")
    #generator.addList("Sample Title", "Sample Text", 
    #    [[1, "First Level"], [2, "Second Level"], [1, "First Level"]])
    #generator.addTable("Sample Table", [["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]])
    #generator.finalize()

    # References:
    # https://python-pptx.readthedocs.io/en/latest/user/quickstart.html