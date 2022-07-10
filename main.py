"""
version 0.2
by Aliaksandr Dvornik
"""

import os
from reader.core import DataInterface
from reader.log_writer import write_logs
import time


file_path = os.path.join(os.path.dirname(__file__), 'sample.spe')

if __name__ == "__main__":
    print("[+] Run programme")
    write_logs("Start programme")
    time.sleep(1)
    data_int = DataInterface()
    cleaned_data = data_int.process_data(file_path)
    data_int.spec_to_dataframe(cleaned_data)
    time.sleep(1)
    print("[+] Converting complete")

