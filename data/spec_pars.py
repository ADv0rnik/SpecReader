class Parser:
# TODO: add more functions
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




#read spectrum file
counts = []
energy_list=[]
counts_in_chanel={}
try:
    inf = open('spec.spe', 'r')
    l = [line.strip() for line in inf]
    del l[:7]

    for i in l:
        date_mea = l[1]
        time = int(l[3].split()[0])
        cps = float(l[5])
        #print(i)
    del l[:15]
    num_of_chanels = int(l[0].split()[1])+1 # reading number of chanels
    counts = [l[i] for i in range(1, num_of_chanels+2)] # reading counts in each chanel
    for a in range(1, num_of_chanels):
        counts_in_chanel[a] = counts[a]
    del l[:1031]
    en = [l[i].split() for i in range(0, num_of_chanels)]
    for elem in en:
        energy_list.append(elem[1])
    # for key, value in counts_in_chanel.items():
    #     print(key, value)

    #for i in range(len(energy_list)):
        #print(energy_list[i], end ='\n')

    # print(time)
    # print(date_mea)
    # print(cps)
    # print(num_of_chanels)

except IOError:
    print("No file")
