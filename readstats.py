import sys
import csv
import numpy as np
import math

S1list = []
S2list = []
with open("examplefbstats.csv",'r') as csvfile:
	reader = csv.reader(csvfile, quotechar='|')
	for row in reader:
		
		try: 
		
			S1 = float(row[13])/float(row[14])
			S2 = float(row[17])/float(row[18])
			S1list.append(S1)
			S2list.append(S2)
		except: pass
S1std = np.std(S1list)
S1avg = np.mean(S1list)

print "S1list",S1list
print "dS1",
dS1 = [ abs(S - S1avg)/S1std for S in S1list ] 
print dS1
print "Avg S1",S1avg
print "Std S1",S1std
