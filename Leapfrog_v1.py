# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:25:49 2016
@author: Matthew
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 6.67408e-11
mSun = 1.9891e30

def initSun():
    return ["Sun", mSun, 0, 0, 0, 0, 0, 0]

def initEarth():
    a = 149.60e9
    e = 0.0167
    x = a*(1+e)
    y = 0
    z = 0
    vx = 0
    vy = np.sqrt((1-e)/(1+e))*np.sqrt((mSun*G)/a)
    vz = 0
    
    return ["Earth", 5.9723e24, x, y, z, vx, vy, vz]
    
def distanceTo(tempCoords, body2):
    distx = tempCoords[0] - body2[2]
    disty = tempCoords[1] - body2[3]
    distz = tempCoords[2] - body2[4]
    return np.sqrt(np.power(distx, 2) + np.power(disty, 2) + np.power(distz, 2))
        
def earthLeap(earthBody, sunBody, dt):
    rList = [earthBody[2], earthBody[3], earthBody[4]]
    vList = [earthBody[5], earthBody[6], earthBody[7]]
    #print("Before Leapfrog:")
    #print(rList)
    #r = np.sqrt(np.power(rList[0], 2) + 
    #np.power(rList[2], 2) + np.power(rList[2], 2))
    
    tempList = [0,0,0]
    for coord in range(3):
        tempList[coord] = rList[coord]  + vList[coord]*(dt/2.0)
    
    distToSun = distanceTo(tempList, sunBody)
        
    accelCoeff = (-G*mSun)/np.power(distToSun, 3)
    
    accelList = [0,0,0]
    for coord in range(3):
        accelList[coord] = tempList[coord]*accelCoeff
        
    for coord in range(3):
        vList[coord] = vList[coord] + accelList[coord]*dt
        
    for coord in range(3):
        rList[coord] = tempList[coord] + vList[coord]*(dt/2.0)
    
    #print("After Leapfrog:")
    #print(rList, "\n")
    
    earthBody[2] = rList[0]
    earthBody[3] = rList[1]
    earthBody[4] = rList[2]
    
    earthBody[5] = vList[0]
    earthBody[6] = vList[1]
    earthBody[7] = vList[2]
    
    return earthBody
    
count = 0
earthBody = initEarth()
sunBody = initSun()
xCoords = []
yCoords = []
zCoords = []
iters=100000
while count < 100000:
    xCoords.append(earthBody[2])
    yCoords.append(earthBody[3])
    zCoords.append(earthBody[4])
    earthBody = earthLeap(earthBody, sunBody, 10000)    
    count += 1
 
fig = plt.figure()
#ax = plt.axes(xlim=(-2e11,2e11), ylim=(-2e11,2e11))
#ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2e11,2e11), ylim=(-2e11,2e11))
ax.grid()
line, = ax.plot([],[], '.', lw=0)

def init():
    line.set_data([],[])
    return line,

x = []
y = []
def animate(i):
    
    x.append(xCoords[i])
    y.append(yCoords[i])
    #x = xCoords[i]
    #y = yCoords[i]
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=iters,
                               interval=2, blit=True)
plt.show(block=False)

   
"""
plt.axis('equal')
plt.axis([-2e11, 2e11, -2e11, 2e11])
ax = plt.gca()
ax.set_autoscale_on(False)
ax.set_axis_bgcolor('white')
plot1 = plt.plot(xCoords, yCoords, 'b.')
plt.show()  
"""

