import os
import queue
import threading
import pandas as pd

from pathlib import Path
from typing import List
from src.processor.data_parser import DataParser


BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.joinpath("src")


def list_files() -> List[str]:
    file_paths = [os.path.join(SRC_DIR, filename)
                  for filename in os.listdir(SRC_DIR)
                  if os.path.isfile(os.path.join(SRC_DIR, filename)) and filename.endswith(".Spe")]

    return file_paths


def runner():
    data_queue = queue.Queue()
    data_parser = DataParser()
    files = list_files()

    threads = [threading.Thread(target=data_parser.read_from_file, args=(file, data_queue, )) for file in files]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    results = {}
    while not data_queue.empty():
        results.update(data_queue.get())

    return results

def save_to_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.transpose()
    df = df.rename(index={df.index[-1]: "LT"})
    df.to_csv(BASE_DIR.joinpath("data.csv"))
    return df


if __name__ == "__main__":
    print("[+] Run program")
    res = runner()
    # print(res)
    save_to_dataframe(res)