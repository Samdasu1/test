from numpy import random
from numpy import concatenate


x = random.normal(loc=0, scale=14,size=(100))
x_2 = random.normal(loc=0, scale=14,size=(100))
x_3 = random.normal(loc=0, scale=13,size=(100))
x_4 = random.normal(loc=0, scale=13.5,size=(100))
x_5 = random.normal(loc=0, scale=15,size=(100))
x_6 = random.normal(loc=0, scale=13,size=(100))
x_7 = random.normal(loc=0, scale=12,size=(100))
x_8 = random.normal(loc=0, scale=14.4,size=(100))
x_9 = random.normal(loc=0, scale=60,size=(100))
x_10 = random.normal(loc=0, scale=80,size=(100))
x_11 = random.normal(loc=0, scale=70,size=(100))
x_12 = random.normal(loc=0, scale=75,size=(100))
x_13 = random.normal(loc=0, scale=67,size=(100))
x_14 = random.normal(loc=0, scale=71,size=(100))
x_15 = random.normal(loc=0, scale=69,size=(100))
x_16 = random.normal(loc=0, scale=71,size=(100))
x_17 = random.normal(loc=0, scale=62,size=(100))
x_18 = random.normal(loc=0, scale=70,size=(100))
x_19 = random.normal(loc=0, scale=55,size=(100))
x_20 = random.normal(loc=0, scale=32,size=(100))
x_21 = random.normal(loc=0, scale=13,size=(100))
x_22 = random.normal(loc=0, scale=13,size=(100))
x_23 = random.normal(loc=0, scale=14,size=(100))
x_24 = random.normal(loc=0, scale=11,size=(100))

import pandas as pd

x_csv=pd.DataFrame(x)
x_2_csv=pd.DataFrame(x_2)
x_3_csv=pd.DataFrame(x_3)
x_4_csv=pd.DataFrame(x_4)
x_5_csv=pd.DataFrame(x_5)
x_6_csv=pd.DataFrame(x_6)
x_7_csv=pd.DataFrame(x_7)
x_8_csv=pd.DataFrame(x_8)
x_9_csv=pd.DataFrame(x_9)
x_10_csv=pd.DataFrame(x_10)
x_11_csv=pd.DataFrame(x_11)
x_12_csv=pd.DataFrame(x_12)
x_13_csv=pd.DataFrame(x_13)
x_14_csv=pd.DataFrame(x_14)
x_15_csv=pd.DataFrame(x_15)
x_16_csv=pd.DataFrame(x_16)
x_17_csv=pd.DataFrame(x_17)
x_18_csv=pd.DataFrame(x_18)
x_19_csv=pd.DataFrame(x_19)
x_20_csv=pd.DataFrame(x_20)
x_21_csv=pd.DataFrame(x_21)
x_22_csv=pd.DataFrame(x_22)
x_23_csv=pd.DataFrame(x_23)
x_24_csv=pd.DataFrame(x_24)



writer=pd.concat([x_csv,x_2_csv],axis=1)
writer2=pd.concat([writer,x_3_csv],axis=1)
writer3=pd.concat([writer2,x_4_csv],axis=1)
writer4=pd.concat([writer3,x_5_csv],axis=1)
writer5=pd.concat([writer4,x_6_csv],axis=1)
writer6=pd.concat([writer5,x_7_csv],axis=1)
writer7=pd.concat([writer6,x_8_csv],axis=1)
writer8=pd.concat([writer7,x_9_csv],axis=1)
writer9=pd.concat([writer8,x_10_csv],axis=1)
writer10=pd.concat([writer9,x_11_csv],axis=1)
writer11=pd.concat([writer10,x_12_csv],axis=1)
writer12=pd.concat([writer11,x_13_csv],axis=1)
writer13=pd.concat([writer12,x_14_csv],axis=1)
writer14=pd.concat([writer13,x_15_csv],axis=1)
writer15=pd.concat([writer14,x_16_csv],axis=1)
writer16=pd.concat([writer15,x_17_csv],axis=1)
writer17=pd.concat([writer16,x_18_csv],axis=1)
writer18=pd.concat([writer17,x_19_csv],axis=1)
writer19=pd.concat([writer18,x_20_csv],axis=1)
writer20=pd.concat([writer19,x_21_csv],axis=1)
writer21=pd.concat([writer20,x_22_csv],axis=1)
writer22=pd.concat([writer21,x_23_csv],axis=1)
writer23=pd.concat([writer22,x_24_csv],axis=1)

writer23.to_csv('data deamnd_2.csv')

A=1