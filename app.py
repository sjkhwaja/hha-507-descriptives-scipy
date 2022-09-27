import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from pandas.plotting import scatter_matrix
from scipy import stats
from statsmodels.formula.api import ols


data = pd.read_csv('https://scipy-lectures.org/_downloads/brain_size.csv', sep = ';', na_values = ".")
data


t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})


data.shape
data.columns
print(data['Gender'])
data[data['Gender'] == 'Female']['VIQ'].mean()


groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

groupby_gender.mean()


scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']]) 


stats.ttest_1samp(data['VIQ'], 0)

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq) 