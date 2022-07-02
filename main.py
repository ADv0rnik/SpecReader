"""
version 0.9.1
by Aliaksandr Dvornik
"""

from reader.core import Parser
from reader.df_constructor import DfConstructor

num_of_channels = 1023

fname = 'spec.spe'
pars = Parser(fname)

# read spectrum file
line = pars.get_lines()
pars.remove_lines(line, 7)

# get reader from spectrum file
date_mea = pars.get_param(line)[0]  # date of measurements
time = pars.get_param(line)[1]  # time of measurements
cps = pars.get_param(line)[2]  # total counts per second
pars.remove_lines(line, 16)

# get list of counts per channel
counts = pars.get_counts(line, num_of_channels)
pars.remove_lines(line, 1030)

# get list of energy
energy = pars.get_energy_list(line, num_of_channels)

# create reader frame
df = DfConstructor()
df.get_dataframe(energy,counts,time)