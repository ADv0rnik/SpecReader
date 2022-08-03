import pandas as pd
import time
import os
from tqdm import tqdm

from reader.reader_logger import write_logs

NUM_CHANNELS = 1023
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__)).replace("/reader", "/output")
FILE_PATH = OUTPUT_DIR + "/spec_data.csv"


class DataProcessor:
    """
    This class define all main functions to parse the spectrum file
    """
    @staticmethod
    def __convert_values(value):
        """
        Simple static method to convert values of string or integer into float

        :param value: value of any type to be converted
        :returns: value - float value
        """
        return float(value)

    @staticmethod
    def __get_lines(file):
        """
        Method allows to read lines from the spectrum file

        :returns: lines, batch of lines from spectrum file (list[str])
        """
        lines = [line.strip() for line in file]
        return lines

    def get_param(self, lines, n=NUM_CHANNELS):
        """
        The method parse all required parameters (see Returns description below) from the spectrum file

        :param lines: list, list of strings from spectrum file
        :param n: int, number of channels. By default, is 1023

        :returns: date_mea - string, date of measurements
                  time - int, duration of measurements performed in seconds
                  cps - float, counts per second
                  counts - list[int], an overall number of counts per channel obtained
                           within one single measurement
                  energy_list - list[int], an energy value in each single channel
        """
        lines = self.__get_lines(lines)
        date_mea = ''
        time_mea = 0
        cps = 0.0
        energy_list, counts = [], []
        try:
            print("[+] Fetching parameters...")
            write_logs("Fetching parameters", "info")
            time.sleep(1)
            pbar = tqdm(total=5, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', colour="green")
            for a, i in enumerate(lines):
                if i == "$DATE_MEA:":
                    date_mea = lines[a + 1]
                    pbar.update(1)
                    time.sleep(0.5)
                    continue
                if i == "$MEAS_TIM:":
                    time_mea = lines[a + 1].split()
                    pbar.update(1)
                    time.sleep(0.5)
                    continue
                if i == "$CPS:":
                    cps = lines[a + 1]
                    pbar.update(1)
                    time.sleep(0.5)
                    continue
                if i == '$DATA:':
                    counts = [int(lines[a + 1]) for a in range(a + 1, n + (a + 2))]
                    pbar.update(1)
                    time.sleep(0.5)
                if i == '$ENER_TABLE:':
                    energy_list = [int(elem[1]) for elem in [lines[a + 1].split() for a in range(a + 1, n + a + 2)]]
                    pbar.update(1)
                    time.sleep(0.5)
        except ValueError as error:
            print(error)
        else:
            return date_mea, self.__convert_values(time_mea[0]), self.__convert_values(cps), counts, energy_list


class DataLoader:
    def __init__(self):
        self.__data_processor = DataProcessor()
        self.__all_params = None

    def set_all_parameters(self, file):
        self.__all_params = self.__data_processor.get_param(file)

    @staticmethod
    def get_dataframe(data):
        """
        Method converts cleaned data from spectrum file to dataframe using pandas library.

        :param data: cleaned data to be processed (tuple)
        :returns: df - pandas object
        """
        energy = data[4]
        counts = data[3]
        time_of_mea = data[1]
        df = pd.Series(energy, counts).to_frame().reset_index()
        df.columns = ['Counts', 'Energy']
        df['CPS'] = df['Counts'] / int(time_of_mea)
        return df

    @property
    def all_params(self):
        return self.__all_params


class DataInterface:
    """
    Class provides an interface to process spectrum data
    """
    def __init__(self):
        self.__data_loader = DataLoader()

    def process_data(self, specfile: str, mode="r") -> tuple:
        try:
            with open(specfile, mode) as file:
                print("[+] Opening spectrum file")
                write_logs("Opening spectrum file", "info")
                time.sleep(1)
                self.__data_loader.set_all_parameters(file)
        except FileNotFoundError as err:
            print(f"[-] An error occurred: {err}")
            write_logs(f"{err}", 'error')
        else:
            return self.__data_loader.all_params

    def spec_to_dataframe(self, clean_data: tuple):
        try:
            dataframe = self.__data_loader.get_dataframe(clean_data)
            dataframe.to_csv(FILE_PATH)
            write_logs("End program", "info")
        except TypeError as t_err:
            print(f"[-] An error occurred: {t_err}")
            write_logs(f"{t_err}", 'error')
