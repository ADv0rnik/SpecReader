import argparse
import os
import queue
import sys
import threading
from email.policy import default

import pandas as pd

from typing import List
from src.processor.data_parser import DataParser
from src.config import FFORMAT, VERSION, OUTPUT_FORMAT
from src.reader_logger import write_logs


def parse_arguments():
    """
    The method determines parser for arguments derived from the CLI.
    Defines all optional and positional arguments such as path, --version and --out

    :returns: arguments passed on CLI script call

    """
    parser = argparse.ArgumentParser(prog='spec-src',
                                     description="List of commands for SpecReader",
                                     epilog="Report about all bugs to aadvornik@gmail.com")
    parser.add_argument(
        "-v",
        "--version",
        help="Show this application's version and exit",
        action="version",
        version=f"SpecReader v.{VERSION}"
    )
    parser.add_argument(
        "-o",
        "--out",
        help="Enable this option to define the output filename",
        type=str,
        default=f'output_data'
    )
    parser.add_argument(
        "Path",
        metavar='path',
        type=str,
        help='The path to spectrum file'
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        help='Format of the spectrum file',
        default=FFORMAT
    )
    return parser.parse_args()


def list_files(source_path: str, file_format: str) -> List[str]:
    file_list = []
    for root, _, files in os.walk(source_path):
        for file in files:
            if file_format in file:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list


def runner():
    print("[+] Run program")
    write_logs("Start program")
    try:
        args = parse_arguments()
    except argparse.ArgumentError as err:
        print(f"[-] Wrong argument: {err}")
        write_logs(f"{err}. End program", 'error')
        sys.exit()
    else:
        data_queue = queue.Queue()
        data_parser = DataParser()
        src_path = args.Path

        if args.out.endswith(OUTPUT_FORMAT):
            output_path = os.path.join(os.path.split(src_path)[0], args.out)
        else:
            output_path = os.path.join(os.path.split(src_path)[0], args.out + OUTPUT_FORMAT)

        if not args.format == FFORMAT:
            format_ = args.format
        else:
            format_ = FFORMAT

        files = list_files(src_path, format_)
        threads = [threading.Thread(target=data_parser.read_from_file, args=(file, data_queue, )) for file in files]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        results = {}
        while not data_queue.empty():
            results.update(data_queue.get())

        save_to_dataframe(output_path, results)


def save_to_dataframe(output_path_name, data):
    try:
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.index += 1
        df = df.rename(index={df.index[-1]: "LT"})
        df.to_csv(output_path_name, mode="w")
    except Exception as err:
        print(f"[-] The data cannot be saved into: {output_path_name}")
        write_logs(f"[-] The data cannot be saved into: {output_path_name} due to {err}", "error")
    else:
        print(f"[+] The data has been saved into: {output_path_name}")
        write_logs(f"[+] The data has been saved into: {output_path_name}", "info")


if __name__ == "__main__":
    runner()
