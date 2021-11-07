"""
executive file
to be continued...
"""
from spec_pars import Parser

if __name__ == '__main__':
    fname = 'spec.spe'
    pars = Parser(fname)
    line=pars.get_lines()

    for i in range(len(line)):
        print(line[i])
