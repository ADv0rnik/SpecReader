'''
version 0.9.1
by Aliaksandr Dvornik
'''

#read spectrum file
counts = []
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
    del l[:1025]
    # for key, value in counts_in_chanel.items():
    #     print(key, value)
    for i in l:
        print(i)
    # print(time)
    # print(date_mea)
    # print(cps)
    # print(num_of_chanels)
except IOError:
    print("No file")
