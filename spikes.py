import csv
from scipy.interpolate import *
import numpy as np
import matplotlib.pyplot as plt

#config for TeX
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def use_pm_polarity(list):
    return [-1 if x == 0 else x for x in list]

def keep_one_addr_with_rng(time, xaddr, yaddr, pol, myxaddr, myyaddr, rng):
    #myxaddr = 3
    #myyaddr = 3
    #xaddr = [1,2,3,4,3,3,6,3]
    #yaddr = [2,8,3,5,3,5,6,3]
    
    x_indexes = [i for i, j in enumerate(xaddr) if myxaddr - rng < j < myxaddr + rng]
    y_indexes = [k for k, l in enumerate(yaddr) if myyaddr - rng < l < myyaddr + rng]
    print('x_indexes: ' + str(x_indexes))
    print('y_indexes: ' + str(y_indexes))
    
    #keep common indexes
    common = [i for i, j in zip(x_indexes, y_indexes) if i == j]
    print('common: ' + str(common))
    #print(xaddr[0:100])
    #print(yaddr[0:100])
    return common

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

def show_polarity(time, pol, common):
    figure_pol = plt.figure()
    subplot_pol = figure_pol.add_subplot(111)
    data_event = [pol[i] for i in common]
    print('data_event: ' + str(data_event))
    raw_x = [time[i] for i in common]
    print('raw_x: ' + str(raw_x))
    subplot_pol.stem(raw_x, data_event, linefmt = 'r-', markerfmt = 'None', basefmt = 'None', label = '_nolegend_')

    #events presentation
    subplot_pol.legend(loc = 'upper left')
    subplot_pol.set_ylabel('$p(x,y,t)$', fontsize = 15)
    subplot_pol.set_xlabel('Time', fontsize = 15)
    subplot_pol.yaxis.grid(linestyle='dotted') #horizontal lines
    #hide axes
    #subplot_pol.axes.get_xaxis().set_ticks([])
    #subplot_pol.axes.get_yaxis().set_ticks([0])

    plt.show()