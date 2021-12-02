import matplotlib.pyplot as plt
import serial
import numpy as np

ser = serial.Serial('COM7', 9600)
y = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101]

df = list()
c = 0

while c<15:
    dat = ser.readline().decode().strip()
    dat = float(dat)
    #dat = dat/1000

    df.append(dat)
    c+=1

    print(dat)

print(df)

plt.hist(df, y,ec = "red")
plt.ylabel('F')
plt.xlabel('C')
plt.title('S')

plt.show()



