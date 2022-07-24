import unittest
from tests import CLEANED_DATA

from reader.core import DataProcessor, DataLoader, DataInterface


class ReaderTests(unittest.TestCase):

    def setUp(self):
        self.data_processor = DataProcessor()
        self.data_loader = DataLoader()
        self.data_interface = DataInterface()

    def test_get_params(self):
        with open("tests/sample_0.spe", "r") as testdata:
            result = self.data_processor.get_param(lines=testdata.readlines())
            self.assertIsInstance(result, tuple)

    def test_get_dataframe(self):
        result = len(self.data_loader.get_dataframe(CLEANED_DATA))
        expected_resul = 1024
        self.assertEqual(result, expected_resul)

    def test_get_params_err(self):
        try:
            with open("tests/sample_1.spe", "r") as testdata:
                result = self.data_processor.get_param(lines=testdata.readlines())
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

    def test_process_data(self):
        try:
            self.data_interface.process_data("sample_2.spe", mode="r")
        except FileNotFoundError as e:
            self.assertEqual(type(e), FileNotFoundError)


