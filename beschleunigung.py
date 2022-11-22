import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import double
from time import sleep

time_list=[]
acceleration_list=[]
#Zugriff auf die row-Daten
with open('./Acceleration.csv', 'r') as daten:
    reader= csv.reader(daten,delimiter=',')

    for zeile in reader:
        try:#Daten REinigen und speichern
          time_list.append(double(zeile[0]))
          acceleration_list.append(double(zeile[1]))
        except:
            continue

#Daten eingeben
def draw_acceleration(time_list,acceleration_list):
  fig,ax = plt.subplots()
  plt.title("Beschleunigung", size="x-large")
  plt.ylabel("a [m/s²]", size="x-large")
  plt.xlabel("t [s]", size="x-large")

  ax.set_xticks([0,500,1000,1500,1950])
  ax.set_xticklabels([0,25,50,75,100],rotation='vertical')

  plt.plot(acceleration_list[25:-25],markersize=6, linewidth=1, color='b', label="Stops")
  plt.legend()
  plt.plot(loc=(0.6,0.8))

  plt.show()
  sleep(10)
  plt.close()
