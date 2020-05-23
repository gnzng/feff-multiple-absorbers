import pandas as pd
import numpy as np
import re
import os 
import datetime as dt
from itertools import islice # i think its not used atm

atom = 'La2' # absorbin atom + number
path = '../../FEFF/Cif/La2Fe23Si3-R3-hex/LaL3/{}/'.format(atom)
files = []
f = open(path+'larchfiles.lar', 'w')

createdsigmas = [] #sigmas which got created from scattering atoms
fefflist = [] #creates feff files with variables and so on 
pathlist = [] # creates variable name for fefflist, put in pathlist in larch
f.write('#\n#{} {}\n'.format(path,dt.datetime.now()))
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'feff0' in i:
        with open(path+i,'r') as file1:
            content = file1.read().replace('\n', '') 
        #print(int(re.findall("\d+", i)[0])) #extract number of present feffpath , important for matching to path parsing information in the 
                                            #next step
        #results =  re.findall('Co|Sm', content) # find scattering atoms adjust if new
        #str1 = ''
        #for n in results:
        #    str1 += n
        #if str1 not in createdsigmas:
        #    createdsigmas.append(str1)
        #execution for pathlist : 
        number = re.findall('\d*\.?\d+',i)[0] # find number to make identifier for each path
        pathlist.append('m2'+atom+'_{}'.format(number))
        ### important to adjust : 
        f.write('m2'+atom+'_{}'.format(number) + '=feffpath(\''+path+'{}\', s02 = \'(3/6)*(amp2)*s02\', e0 = \'de0\', sigma2=\'sigma2_debye(20,370)\', deltar = \'alpha2*reff\')\n'.format(i))
f.close()
#co5_1 = feffpath('calc2/co5/feff0001.dat',s02 = '(4/34)*(amp2)*s02',e0 = 'de0',sigma2 = 'sigma2_debye(300,330)+sig2_co2',deltar = 'alpha2*reff')

print('------')
#print('sigmas:')
#print(*createdsigmas,sep='1 = \n')
print('------')
print('pathlist:')
print(*pathlist, sep=", ")     
print('------')

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
            print('sig2_{}'.format(k[n][6]))
        #print(len(k[0]),len(k[1]),len(k[2]))
    #return k s


