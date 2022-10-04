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

shuffle = np.empty((6,4,3),dtype=float)

for i in range(6):
    for j in range(4):
        shuffle[i][j][0] = CImin[j+i*4]
        shuffle[i][j][1] = demandmean[j+i*4]
        shuffle[i][j][2] = CImax[j+i*4]

import itertools

# 3*8
#shuffle_result = list(itertools.product(shuffle[0],shuffle[1],shuffle[2],shuffle[3],shuffle[4],shuffle[5],shuffle[6],shuffle[7]))

# 4*6
#시간 초과
#shuffle_result = list(itertools.product(shuffle[0][0],shuffle[0][1],shuffle[0][2],shuffle[0][3],shuffle[1][0],shuffle[1][1],shuffle[1][2],shuffle[1][3],shuffle[2][0],shuffle[2][1],shuffle[2][2],shuffle[2][3],shuffle[3][0],shuffle[3][1],shuffle[3][2],shuffle[3][3],shuffle[4][0],shuffle[4][1],shuffle[4][2],shuffle[4][3],shuffle[5][0],shuffle[5][1],shuffle[5][2],shuffle[5][3]))

shuffle_result_1 = list(itertools.product(shuffle[0][0],shuffle[0][1],shuffle[0][2],shuffle[0][3]))

shuffle_result_1 = pd.DataFrame(shuffle_result_1)

shuffle_result_2 = list(itertools.product(shuffle[1][0],shuffle[1][1],shuffle[1][2],shuffle[1][3]))

shuffle_result_2 = pd.DataFrame(shuffle_result_2)

shuffle_result_3 = list(itertools.product(shuffle[2][0],shuffle[2][1],shuffle[2][2],shuffle[2][3]))

shuffle_result_3 = pd.DataFrame(shuffle_result_3)

shuffle_result_4 = list(itertools.product(shuffle[3][0],shuffle[3][1],shuffle[3][2],shuffle[3][3]))

shuffle_result_4 = pd.DataFrame(shuffle_result_4)

shuffle_result_5 = list(itertools.product(shuffle[4][0],shuffle[4][1],shuffle[4][2],shuffle[4][3]))

shuffle_result_5 = pd.DataFrame(shuffle_result_5)

shuffle_result_6 = list(itertools.product(shuffle[5][0],shuffle[5][1],shuffle[5][2],shuffle[5][3]))

shuffle_result_6 = pd.DataFrame(shuffle_result_6)



shuffle_result = pd.concat([shuffle_result_1,shuffle_result_2,shuffle_result_3,shuffle_result_4,shuffle_result_5,shuffle_result_6], axis = 1)

shuffle_result.to_csv('test_result_4x6.csv')

A=1 
