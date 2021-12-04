# Importing Library

import serial
import matplotlib.pyplot as plt

import time

arduino = serial.Serial('COM6', 9600)

#Bins of histogram
y = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101]

#Saving data in list
data_ls = []
c = 0
d = 0
while True:
    if (c == 0):
        d+=1
        while c<1000:
            data = arduino.readline().decode().strip()
            data_ls.append(data)
            print(data)
            c+=1
            if len(data_ls) == 1000:

                print(data_ls)
                plt.hist(data_ls, [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101] , ec="red")
                plt.ylabel('F')
                plt.xlabel('C')
                plt.title('S'  + str(d))     #Count no of histogram
                plt.show()
                plt.draw()

    else:

        data_ls.clear()    #Clearing data of previous list


        c = 0
