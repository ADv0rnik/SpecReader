'''
version 0.9
by Aliaksandr Dvornik
'''

#read spectrum file
inf = open('spec.spe', 'r')
l = [line.strip() for line in inf]
del l[:7]
#print(type(l))
for i in l:
    print(i)
