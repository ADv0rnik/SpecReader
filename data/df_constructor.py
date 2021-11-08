import pandas as pd
import numpy as np

from data.spec_pars import Parser

num_of_chanels = 1023

if __name__ == '__main__':
    fname = 'spec.spe'
    pars = Parser(fname)
    # read spectrum file
    line = pars.get_lines()
    pars.remove_lines(line, 7)
    # get data from spectrum file
    date_mea = pars.get_param(line)[0] #date of measurements
    time = pars.get_param(line)[1] #time of measurements
    cps = pars.get_param(line)[2] #total counts per second
    pars.remove_lines(line, 16)
    #get list of counts per chanel
    counts = pars.get_counts(line, num_of_chanels)
    pars.remove_lines(line, 1030)
    #get list of energy
    energy = pars.get_energy_list(line, num_of_chanels)

    #for i in range(len(energy)):
        #print(energy[i])

    #for i in range(len(line)):
        #print(line[i])




print(dir(pd))
#df = pd.Series()

