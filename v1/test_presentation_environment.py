import unittest
import flexmock
from presentation_environment_TW import Presentation



"""
Call as Py -3 -m unittest test_presentation_environment.py 
"""

class TestPresentation(unittest.TestCase):
    def test_layoutSelect_badType(self):
        """
        layoutSelect wrong type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        data1 = 123
        with self.assertRaises(TypeError):
            result = dummyPres.layoutSelect(data1)

    def test_bad_layoutSelect_badValue(self):
        """
        layoutSelect wrong format
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        data1 = "XXX"
        with self.assertRaises(ValueError):
            result = dummyPres.layoutSelect(data1)

    def test_layoutSelect_titleSelected(self):
        """
        layoutSelect returns good value for title type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('title'), 0)

    def test_layoutSelect_listSelected(self):
        """
        layoutSelect returns good value for list type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('list'), 1)
    
    def test_layoutSelect_pictureSelected(self):
        """
        layoutSelect returns good value for picture type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('picture'), 5)

    def test_layoutSelect_plotSelected(self):
        """
        layoutSelect returns good value for plot type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('plot'), 5)

    def test_layoutSelect_textSelected(self):
        """
        layoutSelect returns good value for text type
        """
        dummyPres = Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('text'), 5)