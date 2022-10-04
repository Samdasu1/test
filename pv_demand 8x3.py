import pandas as pd
import numpy as np

demand = pd.read_csv("Demand_Results.csv")



demandmean = np.empty((24,1),dtype=float)
CImin = np.empty((24,1),dtype=float)
CImax = np.empty((24,1),dtype=float)

for i in range(24):
    for j in range(4):
        demandmean[i] +=  demand['DemandMean'][j+4*i]
        CImin[i] += demand['CIMin'][j+4*i]
        CImax[i] += demand['CIMax'][j+4*i]
        
demandmean = demandmean/4
CImin = CImin/4
CImax = CImax/4

#######################################################
#Shuffle

shuffle = np.empty((3,8,3),dtype=float)

for i in range(3):
    for j in range(8):
        shuffle[i][j][0] = CImin[j+i*8]
        shuffle[i][j][1] = demandmean[j+i*8]
        shuffle[i][j][2] = CImax[j+i*8]

import itertools


shuffle_result_1 = list(itertools.product(shuffle[0][0],shuffle[0][1],shuffle[0][2],shuffle[0][3],shuffle[0][4],shuffle[0][5],shuffle[0][6],shuffle[0][7]))

shuffle_result_1 = pd.DataFrame(shuffle_result_1)

shuffle_result_2 = list(itertools.product(shuffle[1][0],shuffle[1][1],shuffle[1][2],shuffle[1][3],shuffle[1][4],shuffle[1][5],shuffle[1][6],shuffle[1][7]))

shuffle_result_2 = pd.DataFrame(shuffle_result_2)

shuffle_result_3 = list(itertools.product(shuffle[2][0],shuffle[2][1],shuffle[2][2],shuffle[2][3],shuffle[2][4],shuffle[2][5],shuffle[2][6],shuffle[2][7]))

shuffle_result_3 = pd.DataFrame(shuffle_result_3)


shuffle_result = pd.concat([shuffle_result_1,shuffle_result_2,shuffle_result_3], axis = 1)

shuffle_result.to_csv('test_result_8x3.csv')

A=1 
