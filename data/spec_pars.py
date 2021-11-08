class Parser:
    """
    This class define all main functions to parse the spectrum file
    """
    def __init__(self, fileName):
        self.fileName = fileName
        self.fin = open(fileName, 'r')

    def get_lines(self):
        line = [l.strip() for l in self.fin]
        return line

    def get_param(self, line):
        date_mea = ' '
        time = 0
        cps = 0.0
        for i in line:
            date_mea = line[1]
            time = int(line[3].split()[0])
            cps = float(line[5])
        return date_mea, time, cps

    def remove_lines(self, line, n):
        del line[:n]

    def get_counts(self, line, n):
        counts = [line[i] for i in range(0, n + 1)]
        return counts

    def get_energy_list(self, line, n):
        energy_list = []
        en = [line[i].split() for i in range(0, n+1)]
        for elem in en:
            energy_list.append(elem[1])
        return energy_list
