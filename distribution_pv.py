from numpy import random
from numpy import concatenate


x = random.normal(loc=0, scale=0.2,size=(100))
x_2 = random.normal(loc=0, scale=0.3,size=(100))
x_3 = random.normal(loc=0, scale=1.2,size=(100))
x_4 = random.normal(loc=0, scale=2.2,size=(100))
x_5 = random.normal(loc=0, scale=3.1,size=(100))
x_6 = random.normal(loc=0, scale=4,size=(100))
x_7 = random.normal(loc=0, scale=5,size=(100))
x_8 = random.normal(loc=0, scale=3.7,size=(100))
x_9 = random.normal(loc=0, scale=2.9,size=(100))
x_10 = random.normal(loc=0, scale=2.1,size=(100))
x_11 = random.normal(loc=0, scale=0.2,size=(100))


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



writer10.to_csv('data 6 pv.csv')

A=1