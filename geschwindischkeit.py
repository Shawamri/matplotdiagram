import csv
import pandas as pd
import matplotlib.pyplot as plt

from numpy import double

time_list=[]
velocity_list=[]
#Zugriff aud die Row-Daten 
with open('./Pressure and velocity.csv', 'r') as daten:
    reader= csv.reader(daten,delimiter=',')

    for zeile in reader:
        try:
          #Daten auslesen,reinigen und speichern
          time_list.append(double(zeile[-2]))
          velocity_list.append(double(zeile[-1]))
        except:
            continue
#Daten eingeben 
def draw_velocity(time_list,velocity_list):
  fig,ax = plt.subplots()

  plt.title("Geschwindischkeit", size="x-large")
  plt.ylabel("v [m/s]", size="x-large")
  plt.xlabel("t [s]", size="x-large")



  ax.set_xticks([0,25,50,75])
  ax.set_xticklabels([0,25,50,75],rotation='vertical')

  plt.plot(velocity_list,markersize=6, linewidth=1, color='r', label="Stops")
  plt.legend()
  plt.plot(loc=(0.6,0.8))
  plt.show()
  plt.close()
