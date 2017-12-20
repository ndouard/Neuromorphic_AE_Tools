import csv
from scipy.interpolate import *
import numpy as np
import matplotlib.pyplot as plt

#config for TeX
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

def use_pm_polarity(list):
    return [-1 if x == 0 else x for x in list]

def keep_one_addr_with_rng(time, xaddr, yaddr, pol, myxaddr, myyaddr, rng):
    
	#hold address pairs
    addr = []
    for k in range(len(xaddr)):
        addr.append((xaddr[k], yaddr[k]))
    print('All the addresses in loaded data are (showing first 100): ' + str(addr[0:10]))
	
    myaddr = (myxaddr, myyaddr)
    print('My address (x,y) of interest is: ' + str(myaddr))
    
	#x address range
    myaddr_x_rng = []
    for k in range(myxaddr - rng, myxaddr + rng + 1):
        myaddr_x_rng.append(k)
	
	#y address range
    myaddr_y_rng = []
    for k in range(myyaddr - rng, myyaddr + rng + 1):
        myaddr_y_rng.append(k)

	#accepted addresses considering range
    accept_addr = []
    for k in range(len(myaddr_x_rng)):
        for l in range(len(myaddr_y_rng)):
            accept_addr.append((myaddr_x_rng[k], myaddr_y_rng[l]))
    print('Accepted addresses considering a range of ' + str(rng) + ' are: ' + str(accept_addr))		
	    
    #keep indexes of interest in range
    considered = []
    for curr_tested_addr in range(len(accept_addr)):
	    print('Currently testing address: ' + str(accept_addr[curr_tested_addr]))
	    for curr_addr in range(len(addr)):
	        if addr[curr_addr] == accept_addr[curr_tested_addr]:
		        considered.append(curr_addr)
    print('Considered indexes (not ordered/showing first 100 out of ' + str(len(considered) + 1) + ': ' + str(considered[0:100]))
    #exit(0) #remove me
    return considered

def keep_one_addr(time, xaddr, yaddr, pol, myxaddr, myyaddr):
    #myxaddr = 3
    #myyaddr = 3
    #xaddr = [1,2,3,4,3,3,6,3]
    #yaddr = [2,8,3,5,3,5,6,3]
    
    x_indexes = [i for i, j in enumerate(xaddr) if j == myxaddr]
    y_indexes = [i for i, j in enumerate(yaddr) if j == myyaddr]
    print('x_indexes: ' + str(x_indexes))
    print('y_indexes: ' +str(y_indexes))
    
    #keep common indexes
    common = [i for i, j in zip(x_indexes, y_indexes) if i == j]
    print('common: ' + str(common))
    #print(xaddr[0:100])
    #print(yaddr[0:100])
    return common

def plot_polarity(time, pol, common):
    figure_pol = plt.figure()
    subplot_pol = figure_pol.add_subplot(111)
    data_event = [pol[i] for i in common]
    print('data_event (first 100): ' + str(data_event[0:100]))
    raw_x = [time[i] for i in common]
    print('raw_x (first 100): ' + str(raw_x[0:100]))
    subplot_pol.stem(raw_x, data_event, linefmt = 'r-', markerfmt = 'None', basefmt = 'None', label = '_nolegend_')

    #events presentation
    subplot_pol.legend(loc = 'upper left')
	#TODO: add TeX back! $p(x,y,t)$
    subplot_pol.set_ylabel('p(x,y,t)', fontsize = 15)
    subplot_pol.set_xlabel('Time', fontsize = 15)
    subplot_pol.yaxis.grid(linestyle='dotted') #horizontal lines
    #hide axes
    #subplot_pol.axes.get_xaxis().set_ticks([])
    #subplot_pol.axes.get_yaxis().set_ticks([0])

    plt.show()