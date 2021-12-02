#Plotting and reading realtime data from csv

import serial
import time
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animatiom

y = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101]

ser = serial.Serial('COM7', 9600)
ser.flushInput()
t = int(20)
while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer, end="\r")  #overwrite previous line
    time.sleep(1)
    t -= 1
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        with open("test_data3.csv","a") as f:
            writer = csv.writer(f)
            writer.writerow([decoded_bytes])
    except:
        print("Keybord Intrrupt")
        break

data = pd.read_csv('test_data3.csv', sep=',', header=None, index_col = 0)

#data.plot(kind='bar')
plt.hist(data, y,ec = "red")
plt.ylabel('F')
plt.xlabel('C')
plt.title('S')

plt.show()