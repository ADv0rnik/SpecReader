"""
version 0.9.1
by Aliaksandr Dvornik
"""

from data.spec_pars import Parser
from data.df_constructor import DfConstructor

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

# create data frame
df = DfConstructor()
df.get_dataframe(energy,counts,time)

# create GUI
root = tk.Tk()
root.title('SpecReader 0.9.1')

canvas = tk.Canvas(root, width= 800, height=600)
canvas.grid(columnspan = 3, rowspan = 3)

description = tk.Label(root, text='Browse spectrum file', font = 'Raleway')
description.grid(column = 0, row=0)
root.mainloop()
