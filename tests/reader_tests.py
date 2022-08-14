import unittest

import pytest
from tests import CLEANED_DATA, SAMPLE_LIST, DATA_DIR
from reader.reader_core import DataProcessor, DataLoader, DataInterface


@pytest.mark.parametrize("data, num_of_channels, expect", [(SAMPLE_LIST, 9, "TypeError")])
def test_get_params_err(data, num_of_channels, expect):
    data_processor = DataProcessor()
    try:
        data_processor.get_param(lines=data, n=num_of_channels)
    except TypeError as error:
        assert type(error) == expect


@pytest.mark.parametrize("data, num_of_channels, expect", [(SAMPLE_LIST, 9, tuple)])
def test_get_params(data, num_of_channels, expect):
    data_processor = DataProcessor()
    result = data_processor.get_param(lines=data, n=num_of_channels)
    assert type(result) == expect


class ReaderTests(unittest.TestCase):

    def setUp(self):
        self.data_loader = DataLoader()
        self.data_interface = DataInterface()

    def test_get_dataframe(self):
        result = len(self.data_loader.get_dataframe(CLEANED_DATA))
        expected_resul = 6
        self.assertEqual(result, expected_resul)

    def test_process_data(self):
        try:
            self.data_interface.process_data(DATA_DIR + "/sample_2.spe", mode="r")
        except FileNotFoundError as e:
            self.assertEqual(type(e), FileNotFoundError)
