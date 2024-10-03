import unittest
import pytest
from numpy.ma.testutils import assert_equal

from src.processor.data_parser import DataParser
from src.main import save_to_dataframe



@pytest.fixture(scope="session")
def mk_tmp_dir(tmp_path_factory):
    dir_ = tmp_path_factory.mktemp("tmp") / "tmp.csv"
    return dir_


def test_save_to_dataframe(mk_tmp_dir):
    test_dict =  {'test_data.Spe': [0, 0, 0, 0, 0, 14, 907, 2486, 2363, 1972, 1810, 1691, 1767, 2021, 0, 378]}
    test_none = None
    save_to_dataframe(mk_tmp_dir, test_dict)
    save_to_dataframe(mk_tmp_dir, test_none)



class ReaderTests(unittest.TestCase):

    def setUp(self):
        self.data_parser = DataParser()
        self.test_line = "144 146 "

    def test_split_line(self):
        result = self.data_parser.split_line(self.test_line)
        assert_equal(result, ['144', '146'])
        assert_equal(isinstance(result, list), True)
