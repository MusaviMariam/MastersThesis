#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Video Transmitter (GMSK)
# Author: Reproduce by Mariam.
# Generated: Wed Jun 29 21:26:44 2016
##################################################
import poisson_process_v1
from random import *
import time
import random
import numpy as np


print '\n*******************************************************************'
print '\t\t\t    PUs ON & OFF times'
print '*******************************************************************'

No_of_PU = 8;
PU = lambda n: [randint(0,1) for i in range(1, n+1)]
val_PU = PU(No_of_PU)
k = [828e6, 833e6, 838e6, 843e6, 848e6, 853e6, 858e6, 863e6, 868e6, 873e6, 878e6, 883e6, 888e6, 893e6, 898e6, 903e6, 908e6, 913e6, 918e6]
freq_PU = [0, 0, 0, 0, 0, 0, 0, 0];

random_list_PU = random.sample(xrange(19), No_of_PU)

avgON = [10, 10, 10, 10, 10, 10, 10, 10]							# Average ON time is fixed as in 
avgOFF= [15, 15, 15, 15, 15, 15, 15, 15]
times_in_sec = [0,0,0,0,0,0,0,0]
print 'states of PUs', val_PU, '\n'
for i in range(0, len(random_list_PU)): 
	freq_PU[i] = k[random_list_PU[i]]
#		print 'frequency of PU', i, 'is =', freq_PU[i]


for i in range(0, No_of_PU):
	print 'frequency of PU', i, 'is =', freq_PU[i]		
	if val_PU[i] == 1:
		times_in_sec[i] = poisson_process_v1.poisson_process(avgON[i])			
		print 'PU', i, 'is in active state'
		print 'time is =', times_in_sec[i]
	elif val_PU[i] == 0: 
		times_in_sec[i] = poisson_process_v1.poisson_process(avgOFF[i])
		print 'PU', i, 'is in inactive state'
		print 'time is =', times_in_sec[i]
	print '\n'





print '\n*******************************************************************'
print '\t\t\t    Channel Assignment'
print '*******************************************************************'

set_of_links = [[1,2], [1,3], [2,4],[2,5],[3,5],[3,6],[4,7],[5,7],[5,8],[6,8],[7,9],[7,10], [8,10], [8,11], [9,12], [10,12], [10,13], [11,13],[12,13]]
freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
random_list = random.sample(xrange(19), 19)
print 'the number is =', random_list

for i in range(0, len(random_list)): 
	freq[i] = k[random_list[i]]
	print 'frequency', i, 'is =', freq[i], 'for link', set_of_links[i]   

