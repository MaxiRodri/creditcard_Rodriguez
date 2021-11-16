import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

filename =r'C:\Data_Science\creditcard_Rodriguez\creditcard.csv'
data= pd.read_csv(filename)

print(data)