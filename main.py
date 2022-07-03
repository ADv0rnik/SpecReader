"""
version 0.2
by Aliaksandr Dvornik
"""

import os
from reader.core import DataInterface


file_path = os.path.join(os.path.dirname(__file__), 'sample.spe')


if __name__ == "__main__":
    try:
        data_int = DataInterface()
        data_int.process_data(file_path)
    except FileNotFoundError as err:
        print(err)
