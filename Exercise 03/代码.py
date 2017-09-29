import numpy as np 

import matplotlib.pyplot as plt

x = [0.]  
t = [0.] 
v = 40 
dt = 0.1
end_time = 20

for i in range(int(end_time / dt)):

	tmp = x[i] + v * dt

	x.append(tmp)

	t.append(dt * (i + 1))     #euler 法

	print t[-1], x[-1]

plt.figure(figsize=(8,6)) 

plt.plot(t,x,label="x(t)",color="red",linewidth=1)

plt.xlabel("t(s)") 

plt.ylabel("x(m)") 

plt.legend()  

plt.show() 
