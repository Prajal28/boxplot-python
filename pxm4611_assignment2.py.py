import pandas as ps
import matplotlib.pyplot as plot
datafr = ps.read_csv('D:\\UTA\\2nd Sem\\Data Mining\\Homework\\Assignment 02\\go_track_tracks.csv',skiprows=1)
fig, ax = plot.subplots()
datafr.boxplot(ax=ax, positions=[1,2,3,4,5,6,7,8], notch=True, bootstrap=7500)
ax.set_xticks(range(9))
ax.set_xticklabels(['0','ID_Android','Speed','Time','Distance','Rating','Rating_Bus','Rating_Weather','Car_or_Bus'])
plot.xticks(rotation=35)
plot.show()
