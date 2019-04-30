import unittest
import flexmock
import presentation_environment_TW


"""
Call as Py -3 -m unittest test_presentation_environment.py 
"""




class TestPresentation(unittest.TestCase):
    def test_layoutSelect_badType(self):
        """
        layoutSelect wrong type
        """

        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        
        data1 = 123
        with self.assertRaises(TypeError):
            result = dummyPres.layoutSelect(data1)

    def test_bad_layoutSelect_badValue(self):
        """
        layoutSelect wrong format
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        data1 = "XXX"
        with self.assertRaises(ValueError):
            result = dummyPres.layoutSelect(data1)

    def test_layoutSelect_titleSelected(self):
        """
        layoutSelect returns good value for title type
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('title'), 0)

    def test_layoutSelect_listSelected(self):
        """
        layoutSelect returns good value for list type
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('list'), 1)
    
    def test_layoutSelect_pictureSelected(self):
        """
        layoutSelect returns good value for picture type
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('picture'), 5)

    def test_layoutSelect_plotSelected(self):
        """
        layoutSelect returns good value for plot type
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('plot'), 5)

    def test_layoutSelect_textSelected(self):
        """
        layoutSelect returns good value for text type
        """
        flexmock(presentation_environment_TW.presentation_generator_TW.PresentationGenerator).should_receive('__new__').once()
        dummyPres = presentation_environment_TW.Presentation('PYTHON-Environment.pptx','PYTHON-Course.template')
        self.assertEqual(dummyPres.layoutSelect('text'), 5)