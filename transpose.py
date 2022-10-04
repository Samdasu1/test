import pandas as pd
import numpy as np

df = pd.read_csv("test_result_8x3.csv")


X = df.transpose()

X.to_csv('test transpose.csv')