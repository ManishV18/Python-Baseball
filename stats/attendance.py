import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance =games[(games['type'] == 'info') & (games['multi2']== 'attendance')]
attendance = attendance[['year','multi3']]
attendance.columns = ['year','attendance']
selection = attendance.loc[:,'attendance']
selection = pd.to_numeric(selection)

plt.plot(attendance['year'], attendance['attendance'])
plt.show()
