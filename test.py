import csv
from time import sleep

from numpy import double

from beschleunigung import draw_acceleration
from geschwindischkeit import draw_velocity

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

acceleration_list=[]
#Zugriff auf die row-Daten
with open('./Acceleration.csv', 'r') as daten:
    reader= csv.reader(daten,delimiter=',')

    for zeile in reader:
        try:#Daten reinigen und speichern
          acceleration_list.append(double(zeile[1]))
        except:
            continue

#Daten darstellen:
#first Test
draw_acceleration(time_list,acceleration_list)
#Second Test
draw_velocity(time_list,velocity_list)

