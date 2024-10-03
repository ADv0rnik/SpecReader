import unittest

import pandas as pd
import pytest

from src.processor.data_parser import DataParser
from src.main import save_to_dataframe, parse_arguments
from argparse import Namespace


@pytest.fixture(scope="session")
def mk_tmp_dir(tmp_path_factory):
    dir_ = tmp_path_factory.mktemp("tmp") / "tmp.csv"
    return dir_


def test_save_to_dataframe(mk_tmp_dir):
    test_data =  {'test_data.Spe': [0, 0, 0, 0, 0, 14, 907, 2486, 2363, 1972, 1810, 1691, 1767, 2021, 0, 378]}
    result = save_to_dataframe(mk_tmp_dir, test_data)
    assert type(result) == pd.DataFrame


class ReaderTests(unittest.TestCase):

    def setUp(self):
        self.data_parser = DataParser()
