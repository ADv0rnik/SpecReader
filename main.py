"""
version 0.9.1
by Aliaksandr Dvornik
"""

from data.spec_pars import Parser

if __name__ == '__main__':
    fname = 'spec.spe'
    pars = Parser(fname)
    line = pars.get_lines()
    pars.remove_lines(line, 7)
    # get data from spectrum file
    date_mea = pars.get_param(line)[0] #date of measurements
    time = pars.get_param(line)[1] #time of measurements
    cps = pars.get_param(line)[2] #total counts per second



    for i in range(len(line)):
        print(line[i])
