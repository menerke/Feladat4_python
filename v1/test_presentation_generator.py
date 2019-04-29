import unittest
import flexmock
from presentation_generator_TW import PresentationGenerator
import numpy as np

"""
Call as Py -3 -m unittest test_presentation_generator.py 
"""

class TestPresentationGenerator(unittest.TestCase):
    def test_outputFileName_badType(self):
        """
        outputFileName wrong type
        """
        data1 = 123
        data2 = "a.template"
        with self.assertRaises(TypeError):
            result = PresentationGenerator(data1, data2)

    def test_templateFileName_badType(self):
        """
        templateFileName wrong type
        """
        data1 = "a.pptx"
        data2 = 123
        with self.assertRaises(TypeError):
            result = PresentationGenerator(data1, data2)

    def test_outputFileName_badFormat(self):
        """
        outputFileName wrong format
        """
        data1 = "ASD"
        data2 = "a.template"
        with self.assertRaises(ValueError):
            result = PresentationGenerator(data1, data2)

    def test_templateFileName_badFormat(self):
        """
        templateFileName wrong format
        """
        data1 = "a.pptx"
        data2 = "ASD"
        with self.assertRaises(ValueError):
            result = PresentationGenerator(data1, data2)

    def test_addTitle_returnTrue(self):
        """
        True addTitle in case of correctly supplied data
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertTrue(dummyPres.addTitle(0, "Asd", "Fgh"))

    def test_addList_returnTrue(self):
        """
        True addList  in case of correctly supplied data
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertTrue(dummyPres.addList(1, "Asd",  np.array([1, 1, 2]),np.array(['lvl1', 'lvl1', 'lvl2'])))

    def test_addImage_returnTrue(self):
        """
        True addImage  in case of correctly supplied data
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertTrue(dummyPres.addImage(5, "Asd", 'picture.png'))

    
    def test_addText_returnTrue(self):
        """
        True addText  in case of correctly supplied data
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertTrue(dummyPres.addText(5, "Asd", 'XXXYYYZZZ'))


    def test_addTitle_CorrectTitle(self):
        """
        Correct Title content for AddTitle -> Could be done for others similarly -- left out due to time constraints in this project!
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        dummyPres.addTitle(0, "Asd", "Fgh")
        self.assertEqual(dummyPres._presentation.slides[-1].shapes.title.text, "Asd")

    
    def test_addTitle_CorrectSubTitle(self):
        """
        Correct SubTitle content for AddTitle -> Could be done for others similarly -- left out due to time constraints in this project!
        """
        dummyPres = PresentationGenerator('PYTHON-Environment.pptx','PYTHON-Course.template')
        dummyPres.addTitle(0, "Asd", "Fgh")
        self.assertEqual(dummyPres._presentation.slides[-1].placeholders[1].text, "Fgh"     ) 
        