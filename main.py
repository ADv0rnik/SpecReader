'''
version 0.9
by Aliaksandr Dvornik
'''

#read spectrum file
try:
    inf = open('spec.spe', 'r')
    l = [line.strip() for line in inf]
    del l[:7]
#print(type(l))
    for i in l:
        date_mea = l[1]
        cps = float(l[5])
        #print(i)
    del l[:15]
    for i in l:
        print(i)
    #print(date_mea)
    #print(cps)
except IOError:
    print("No file")
