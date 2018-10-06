import numpy as np
import pandas as pd
from Get_Csv import Get_Csv_task1 as Sheet

data = Sheet()

data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d %H:%M:%S.%f")

data.index = pd.to_datetime(data['Date'],data.index)

#data = pd.read_csv('rawpvr_2018-02-01_28d_1083 TueFri.csv')

c = data[
    (data['Direction Name'] == 'North') &
    (data['Flag Text'] == 'TUESDAY') &
    (data['Date'].index.hour == 9)
]

f = c.groupby(c.index.strftime('%Y-%m-%d')).size().to_frame('size')

range = int(f.max()- f.min())
first = int(f.quantile(0.25))
second = int(f.quantile(0.50))
third = int(f.quantile(0.75))
IQ = int(third - first)

print('range is',range)
print('1st Quartile is',first)
print('2nd Quartile is',second)
print('3rd Quartile is',third)
print('Interquartile range is',IQ)