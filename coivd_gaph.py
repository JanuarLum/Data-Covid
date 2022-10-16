import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import pmdarima as pm

link_covid_data= 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
raw_data = pd.read_csv(link_covid_data)

indonesia = raw_data[raw_data['location'] == 'Indonesia']
spain = raw_data[raw_data['location'] == 'Spain']
poland = raw_data[raw_data['location'] == 'Poland']
argentina = raw_data[raw_data['location'] == 'Argentina']

indonesia2 = indonesia[indonesia['date'] >= '2020-02-24']
spain2 = spain[spain['date'] >= '2020-02-24']
poland2 = poland[poland['date'] >= '2020-02-24']
argentina2 = argentina[argentina['date'] >= '2020-02-24']

plt.plot(indonesia2['date'], indonesia2['total_deaths'])
plt.plot(spain2['date'], spain2['total_deaths'])
plt.plot(poland2['date'], poland2['total_deaths'])
plt.plot(argentina2['date'], argentina2['total_deaths'])
plt.legend(['Indonesia', 'Spain', 'Poland', 'Argentina'])
plt.xticks([30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450], rotation = 'vertical')
plt.title("Data Covid")
#plt.grid()
plt.show()
