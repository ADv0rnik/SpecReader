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
        cps = float(l[5])
        #print(i)
    del l[:15]
    num_of_chanels = int(l[0].split()[1])+1
    counts = [l[i] for i in range(1, num_of_chanels+2)]
    for a in range(1, num_of_chanels):
        counts_in_chanel[a] = counts[a]
    # for key, value in d.items():
    #     print(key, value)
    for i in l:
        print(i)
    #print(date_mea)
    #print(cps)
    #print(num_of_chanels)
except IOError:
    print("No file")
