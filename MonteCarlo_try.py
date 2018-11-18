import numpy as np
import matplotlib.pyplot as plt
import math
import random as random

t = np.arange(0,np.pi/2, 0.01)
r = 1
x1 = r*np.cos(t)  
y1 = r*np.sin(t) 

t_i = 50000
x = np.zeros(t_i)
y = np.zeros(t_i)
print len(x)
for i in range(0, t_i):
	x[i] = random.uniform(0,1.0)
	y[i] = random.uniform(0,1.0)

inside = 0.0
for i in range(0, len(x)):
	value = (x[i])**2 + (y[i])**2
	if value <= r:
		inside = inside + 1
	
outside = t_i - inside
area = 4*(inside/t_i)
percent_off = abs(np.pi-area)/np.pi*100
print inside
print area
print percent_off, '% off from pi'

plt.scatter(x,y)
plt.plot(x1, y1,'r')
plt.show()
