import unittest
import flexmock
from presentation_generator_TW import PresentationGenerator

class TestPresentationGenerator(unittest.TestCase):
    def test_bad_outputFileName_type(self):
        """
        outputFileName wrong type
        """
        data1 = 123
        data2 = "a.template"
        with self.assertRaises(TypeError):
            result = PresentationGenerator(data1, data2)

    def test_bad_templateFileName_type(self):
        """
        outputFileName wrong type
        """
        data1 = "a.pptx"
        data2 = 123
        with self.assertRaises(TypeError):
            result = PresentationGenerator(data1, data2)

    def test_bad_outputFileName_format(self):
        """
        outputFileName wrong format
        """
        data1 = "ASD"
        data2 = "a.template"
        with self.assertRaises(ValueError):
            result = PresentationGenerator(data1, data2)

    def test_bad_templateFileName_format(self):
        """
        templateFileName wrong type
        """
        data1 = "a.pptx"
        data2 = "ASD"
        with self.assertRaises(ValueError):
            result = PresentationGenerator(data1, data2)

    # def test_list_int(self):
    #     """
    #     Test that it can sum a list of integers
    #     """
    #     data = [1, 2, 3]
    #     result = sum(data)
    #     self.assertEqual(result, 6)

    # def test_list_fraction(self):
    #     """
    #     Test that it can sum a list of fractions
    #     """
    #     data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    #     result = sum(data)
    #     self.assertEqual(result, Fraction(9, 10))

    # def test_bad_type(self):
    #     """
    #     Test unsupported type
    #     """
    #     data = "banana"
    #     with self.assertRaises(TypeError):
    #         result = sum(data)