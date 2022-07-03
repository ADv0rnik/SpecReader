NUM_CHANNELS = 1023


class DataProcessor:
    """
    This class define all main functions to parse the spectrum file
    """
    @staticmethod
    def __convert_values(value):
        return float(value)

    @staticmethod
    def __get_lines(file):
        """
        Method allows to read lines from the spectrum file
        Returns
        -------
        lines: list[str], batch of lines from spectrum file
        """
        lines = [line.strip() for line in file]
        return lines

    def get_param(self, file, n=NUM_CHANNELS):
        """
        The method parse all necessary parameters (see Returns description below) from the spectrum file
        Parameters:
        -----------
        line: string, batch of strings from spectrum file
        n: int, number of channels
        Returns:
        -------
        date_mea: string, date of measurements
        time: int, duration of measurements performed in seconds
        cps: float, counts per second
        counts: list[int], an overall number of counts per channel obtained
                within one single measurement
        energy_list: list[int], an energy value in each single channel
        """
        lines = self.__get_lines(file)
        date_mea = ''
        time_mea = 0
        cps = 0.0
        energy_list, counts = [], []
        try:
            for a, i in enumerate(lines):
                if i == "$DATE_MEA:":
                    date_mea = lines[a + 1]
                    continue
                if i == "$MEAS_TIM:":
                    time_mea = lines[a + 1].split()
                    continue
                if i == "$CPS:":
                    cps = lines[a + 1]
                    continue
                if i == '$DATA:':
                    counts = [int(lines[a + 1]) for a in range(a + 1, n + (a + 2))]
                if i == '$ENER_TABLE:':
                    energy_list = [int(elem[1]) for elem in [lines[a + 1].split() for a in range(a + 1, n + a + 2)]]
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

    @property
    def all_params(self):
        print()
        return self.__all_params


class DataInterface:
    """
    Class provides an interface to process spectrum data
    """
    def __init__(self):
        self.__data_loader = DataLoader()

    def process_data(self, specfile: str, mode="r"):
        try:
            with open(specfile, mode) as file:
                self.__data_loader.set_all_parameters(file)
        except FileNotFoundError as err:
            print(err)
        else:
            return self.__data_loader.all_params
