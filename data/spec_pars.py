import re


class Parser:
    """
    This class define all main functions to parse the spectrum file
    """

    def __init__(self, file_name):
        self.fileName = file_name

    def get_lines(self):
        with open(self.fileName, "r") as f:
            line = [l.strip() for l in f]
        return line

    def get_cps(self, line):
        for a, j in enumerate(line):
            if j == '$CPS:':
                return float(line[a + 1])

    def get_param(self, line):
        date_mea = ' '
        time = 0
        cps = 0.0
        for _ in line:
            date_mea = re.match(r'\d{2}/\d{2}/\d{4}', line)
            # date_mea = line[1]
            time = int(line[3].split()[0])
            cps = float(line[5])
        return date_mea, time, cps

    def remove_lines(self, line, n):
        del line[:n]

    def get_counts(self, line, n):
        counts = [int(line[i]) for i in range(0, n + 1)]
        return counts

    def get_energy_list(self, line, n):
        energy_list = []
        en = [line[i].split() for i in range(0, n + 1)]
        for elem in en:
            energy_list.append(int(elem[1]))
        return energy_list


num_of_channels = 1023

fname = "C:\\Users\\aadvo\\PycharmProjects\\SpecReader\\spec.spe"

# match = re.search(r'\d{2}/\d{2}/\d{4}', line)
# if match:
#     print(match[0])
pars = Parser(fname)
cps = pars.get_cps(pars.get_lines())


