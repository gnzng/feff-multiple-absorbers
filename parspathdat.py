import pandas as pd
import numpy as np
import re
import os 
import datetime as dt
from itertools import islice # i think its not used atm

path = 'testfiles/'
########
####
#extra teil der pfadinformation auslesen kann, hilfreich für sigma2 berechnung ? ? ? ? ? ? 
####
def readpath(a):
    with open(path+'paths.dat','r') as file2:
        k = []
        for line in file2:
            if 'index' in line:
                t = line[:9]
                t = int(t)
            if '0.0000' in line:
                if t == a:
                    k.append(line.replace('\'','').replace('\n','').split())
        k = np.array(k)
        for n in range(len(k)-1):
            print('sig2_{}*{}'.format(k[n][4],k[n][5]))
readpath(1)

