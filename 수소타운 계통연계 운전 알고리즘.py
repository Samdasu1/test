import gurobipy as gp
from gurobipy import GRB
import pandas as pd
import numpy as np
import data_get

#pandas로 작업
ess_config = data_get.ess_config
peak_price = data_get.peak_price
tou_price = data_get.tou_price
demand = data_get.demand
pv = data_get.pv
Tank = data_get.Hydrogen
H2_tou = data_get.H2_tou

demand_time = demand.iloc[:,1:4]
opt_index = demand.iloc[0,0]
demand_mean = demand.iloc[:,5]
#PV classfication flexibility 수정해야함
if pv.iloc[1,0] == 2:
    pv_power = pv.iloc[:,5]
    load = demand_mean-pv_power
else:
    load = demand_mean

peak_tou_price = peak_price.iloc[0,2]
ESS_capacity = ess_config.iloc[0,2]
ESS_min = np.array(ess_config.iloc[0,5] * ESS_capacity/100, dtype=np.float64)
ESS_max = np.array(ess_config.iloc[0,6] * ESS_capacity/100, dtype=np.float64)
ESS_charge_ub = np.array(ess_config.iloc[0,7], dtype=np.float64)
ESS_charge_lb = np.array(ess_config.iloc[0,8], dtype=np.float64)
ESS_init = np.array(ess_config.iloc[0,3] * ESS_capacity/100, dtype=np.float64)
Tank_capacity = Tank.iloc[0,2]
Tank_init = np.array(Tank.iloc[0,3]*Tank_capacity/100, dtype=np.float64)
Tank_min = np.array(Tank.iloc[0,4]*Tank_capacity/100, dtype=np.float64)
Tank_max = np.array(Tank.iloc[0,5]*Tank_capacity/100, dtype=np.float64)

#####
#수소 충방전 최대 최소양 boundary 필요한가? 아직은 모름
#Tank_charge_ub = np.array(Tank[0,6], dtype=np.float64)
#Tank_charge_lb = np.array(Tank[0,7], dtype=np.float64)
#####

opt_tou = tou_price.iloc[:,5]
opt_H2_tou = H2_tou.iloc[:,5]

ESS_charge_upper_bound = np.empty((len(load),1),dtype=float)
ESS_charge_lower_bound = np.empty((len(load),1),dtype=float)
ELFC_power_upper_bound = np.empty((len(load),1),dtype=float)
ELFC_power_lower_bound = np.empty((len(load),1),dtype=float)
ESS_SoC = np.empty((len(load),1),dtype=float)
min_SoC = np.empty((len(load),1),dtype=float)
max_SoC = np.empty((len(load),1),dtype=float)
Tank_SoC = np.empty((len(load),1),dtype=float)
max_Tank = np.empty((len(load),1),dtype=float)
min_Tank = np.empty((len(load),1),dtype=float)
reverse_power_flow = np.empty((len(load),1),dtype=float)

for i in range(len(load)):
    ESS_charge_upper_bound[i][0] = ESS_charge_ub
    ESS_charge_lower_bound[i][0] = ESS_charge_lb
    ESS_SoC[i][0] = ESS_init
    min_SoC[i][0] = ESS_min
    max_SoC[i][0] = ESS_max
    Tank_SoC[i][0] = Tank_init
    min_Tank[i][0] = Tank_min
    max_Tank[i][0] = Tank_max
    #reverse_power_flow[i][0] = 0

ESS_eff = (ess_config.iloc[0,9]+ess_config.iloc[:,10])/200

m = gp.Model("test")

plan = range(len(load))

ESS_power = m.addVars(plan,lb=ESS_charge_lower_bound,ub=ESS_charge_upper_bound, vtype = GRB.INTEGER, name="ESS Power")
FC_power = m.addVars(plan, vtype = GRB.INTEGER, name="FC Power")
EL_power = m.addVars(plan, vtype = GRB.INTEGER, name="EL Power")
reverse_power_flow = m.addVars(plan, vtype = GRB.INTEGER, name="Reverse power flow")
power_flow = m.addVars(plan, vtype = GRB.INTEGER, name="power flow")


FC_Start = m.addVars(plan, lb=-1, ub=0, vtype=GRB.INTEGER,name="FC Start")
FC_State = m.addVars(plan, lb=0, ub=1, vtype=GRB.INTEGER, name="FC State")
FC_Shutdown = m.addVars(plan, lb=0, ub=1, vtype=GRB.INTEGER, name="FC Shutdown")

EL_Start = m.addVars(plan, lb=-1, ub=0, vtype=GRB.INTEGER, name="EL Start")
EL_State = m.addVars(plan, lb=0, ub=1, vtype=GRB.INTEGER, name="EL State")
EL_Shutdown = m.addVars(plan, lb=0, ub=1, vtype=GRB.INTEGER, name="EL Shutdown")

######
# FC POWER는 10
# EL POWER는 30으로 가정
# 수소 생산량도 대충 때움
# 수소 비용은 2020년 기준 1kg 당 천연가스 기준 약 2000원 / 재생에너지 기반 1만원
# 수소타운에 들어갈 수소 비용은 천연가스 기준으로 
######

Pre_peak_load = peak_price.iloc[0,1]
Peak_load = m.addVar(lb = Pre_peak_load, name="Peak load")

for _ in range(len(load)):
  ESS_SoC = gp.quicksum(ESS_power[t] for t in range(_+1)) + ESS_init
  m.addConstrs(ESS_SoC<=max_SoC[t] for t in range(_))
  m.addConstrs(0<=ESS_SoC-min_SoC[t] for t in range(_))
  #Peak load 제약
  m.addConstr((ESS_power[_]+load[_]-FC_power[_]+EL_power[_])<=Peak_load)
  #m.addConstr((Pre_peak_load<=Peak_load))
  #FC 제약(state 제약)
  m.addConstrs(FC_Start[t]<=FC_State[t]-FC_State[t+1] for t in range(_))
  m.addConstrs(FC_State[t]-FC_State[t+1]<=FC_Shutdown[t] for t in range(_))
  m.addConstr(-FC_Start[_]+FC_State[_]+FC_Shutdown[_]<=2)
  m.addConstr(FC_Start[0]<=-FC_State[0])
  #FC 제약(state 따른 발전량 제약)
  m.addConstrs(FC_power[t]<=FC_State[t]*10-(-FC_Start[t]+FC_Shutdown[t])*5 for t in range(_))
  m.addConstrs(FC_State[t]*5<=FC_power[t] for t in range(_))

  #FC 제약(최소 가동 시간)
  #FC 이 제약 부분 수정 필요 -> Start를 무조건 하고, State로 넘어가는것
  #(이렇게 하면 뒤에 6시간은 가동을 할 수 없는 상황이 발생)
  #선형화를 하는 작업에서 불가피하게 발생하는 상황이며, 24시간의 스케줄을 원하면 최소 30시간 이상의 스케줄을 얻음으로써 이를 피할 수 있음
  #선형화를 하였기 때문에, 24시간이나 36시간 48시간 스케줄을 계산하는 것은 계산시간이 그렇게 오랜 시간 소요 되지 않을 것으로 생각함
  m.addConstrs(-FC_Start[t]*3<=FC_State[t]+FC_State[t+1]+FC_State[t+2] for t in range(_-2))
  #Infeasible
  ##m.addConstrs(5<=FC_State[t+1]+FC_State[t+2]+FC_State[t+3]+FC_State[t+4]+FC_State[t+5] for t in range(_-5))

  #EL 제약(state 제약)

  m.addConstrs(EL_Start[t]<=EL_State[t]-EL_State[t+1] for t in range(_))
  m.addConstrs(EL_State[t]-EL_State[t+1]<=EL_Shutdown[t] for t in range(_))
  m.addConstr(-EL_Start[_]+EL_State[_]+EL_Shutdown[_]<=2)
  m.addConstr(EL_Start[0]<=-EL_State[0])
  #EL 제약(state 따른 발전량 제약)
  m.addConstrs(EL_power[t]<=EL_State[t]*30-(-EL_Start[t]+EL_Shutdown[t])*15 for t in range(_))
  m.addConstrs(EL_State[t]*15<=EL_power[t] for t in range(_))

  #EL 제약(최소 가동 시간)
  #(이렇게 하면 뒤에 6시간은 가동을 할 수 없는 상황이 발생)
  #선형화를 하는 작업에서 불가피하게 발생하는 상황이며, 24시간의 스케줄을 원하면 최소 30시간 이상의 스케줄을 얻음으로써 이를 피할 수 있음
  #선형화를 하였기 때문에, 24시간이나 36시간 48시간 스케줄을 계산하는 것은 계산시간이 그렇게 오랜 시간 소요 되지 않을 것으로 생각함
  m.addConstrs(-EL_Start[t]*3<=(EL_State[t]+EL_State[t+1]+EL_State[t+2]) for t in range(_-2))
  

  Tank_SoC = gp.quicksum(FC_power[t]*(-0.3)+EL_power[t]*(0.1) for t in range(_+1)) + Tank_init
  
  m.addConstrs(Tank_SoC<=max_Tank[t] for t in range(_))
  m.addConstrs(0<=Tank_SoC-min_Tank[t] for t in range(_))

  m.addConstrs(reverse_power_flow[t]>=0 for t in range(_))
  m.addConstrs(reverse_power_flow[t]>=-(load[t]+ESS_power[t]-FC_power[t]+EL_power[t]) for t in range(_))

  m.addConstrs(power_flow[t]>=0 for t in range(_))
  m.addConstrs(power_flow[t]>=(load[t]+ESS_power[t]-FC_power[t]+EL_power[t]) for t in range(_))


B=1
power = sum(power_flow[t]*opt_tou[t]+Peak_load*peak_tou_price+FC_power[t]*opt_H2_tou[t]+0.0001*(ESS_power[t]**2+FC_power[t]**2+EL_power[t]**2)+reverse_power_flow[t]*opt_tou[t]*400+power_flow[t]+reverse_power_flow[t]-0.00001*(FC_Start[t]+EL_Start[t])+0.00001*(FC_Shutdown[t]+EL_Shutdown[t]) for t in range(len(load)))
#power = sum(reverse_power_flow[t]*opt_tou[t]+Peak_load*peak_tou_price+(FC_power[t]*opt_H2_tou[t])+ESS_power[t]**2*0.01+FC_power[t]**2*0.01+EL_power[t]**2*0.01 for t in range(len(load)))

m.ModelSense = GRB.MINIMIZE
m.setObjective(power)                               

m.optimize()
#m.printStats()
vars = m.getVars()



writer = np.zeros((len(load),11))
np.empty((len(load),1),dtype=float)

for i in range(11):
    for w in range(len(load)):
        writer[w,i] = vars[w+i*len(load)].x

        

    #print('%s %g' % (v.varName, v.Peak_load))



print(m.getObjective())

writer = pd.DataFrame(writer)
writer.to_csv('result compare.csv')

writer2 = pd.DataFrame(load)
writer2.to_csv('load compare.csv')

A=1

