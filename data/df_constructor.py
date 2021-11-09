import pandas as pd
from data.spec_pars import Parser


class DfConstructor:

    def __init__(self):
        pass

    def get_dataframe(self, list1, list2):
        df = pd.Series(list1, list2).to_frame().reset_index()
        df.columns = ['Energy', 'Counts']


num_of_channels = 1023

fname = 'spec.spe'
pars = Parser(fname)
# read spectrum file
line = pars.get_lines()
pars.remove_lines(line, 7)
# get data from spectrum file
date_mea = pars.get_param(line)[0]  # date of measurements
time = pars.get_param(line)[1]  # time of measurements
cps = pars.get_param(line)[2]  # total counts per second
pars.remove_lines(line, 16)
# get list of counts per channel
counts = pars.get_counts(line, num_of_channels)
pars.remove_lines(line, 1030)
# get list of energy
energy = pars.get_energy_list(line, num_of_channels)
