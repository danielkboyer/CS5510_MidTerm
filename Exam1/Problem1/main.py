

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

v= 20
t_list = [1, 0.1, 0.01]
max_time =10

L = 4
alpha = np.pi/6
R = 4/np.tan(alpha)
V = 20
Psi_dot = V*np.tan(alpha)/L


TWOPI = 2*np.pi

fig, ax = plt.subplots()
all_x =[]
all_y =[]
for t_setp in t_list:
    # t = np.arange(0.0, t_setp, max_time)
    
    dt = np.arange(0.0, max_time,t_setp)
    print(t_setp)
    print(dt)
    # for dt in range()
    psi = Psi_dot *dt
    x = -v *np.sin(psi) *dt
    y = v* np.cos(psi) *dt
    
    
    # ax = fig.add_subplot(111)
    
    
    ax.plot(x, y)
    
    all_x = np.append(all_x,x)
    all_y = np.append(all_y,y)


lgd = ax.legend([ 'Lag ' + str(lag.size) for lag in all_x])

plt.show()

