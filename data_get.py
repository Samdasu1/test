import os
import pandas as pd
#==================================================================================
# 데이터 통합
#==================================================================================

try:
    ess_config = pd.read_csv(".\input_A\essConfig.csv")
except Exception as e:
    print("Can't found essConfig")
    raise AdminError()

try:
    peak_price = pd.read_csv(".\input_A\peakprice.csv")
except Exception as e:
    print("Can't found peakprice")
    raise AdminError()

try:
    tou_price = pd.read_csv(".\input_A\\tou.csv")
except Exception as e:
    print("Can't found tou")
    raise AdminError()

try:
    demand = pd.read_csv(".\input_A\Demand_ResultData.csv")
except Exception as e:
    print("Can't found Demand_ResultData")
    raise AdminError()

try:
    pv = pd.read_csv(".\input_A\PV_ResultData.csv")
except Exception as e:
    print("Can't found PV_ResultData")
    raise AdminError()

try:
    Hydrogen = pd.read_csv(".\input_A\Hydrogen.csv")
except Exception as e:
    print("Can't found Hydrogen")
    raise AdminError()

try:
    H2_tou = pd.read_csv(".\input_A\H2_tou.csv")
except Exception as e:
    print("Can't found AOS")
    raise AdminError()