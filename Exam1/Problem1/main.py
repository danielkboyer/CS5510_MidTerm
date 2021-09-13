

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

v= 20
t_list = [1, 0.1, 0.01]
max_time =10

L = 4
alpha = -np.pi/6
R = 4/np.tan(alpha)
V = 20
Psi_dot = (V * np.tan(alpha)) / L

all_x =[]
all_y =[]
fig = plt.figure()
ax = fig.add_subplot(111)

for t_setp in t_list:
    # t = np.arange(0.0, t_setp, max_time)
    x = 0 
    y = 0
    psi = 0 
    xlist =[]
    ylist =[]
    for dt in np.arange(0.0, max_time,t_setp):
        # for dt in range()
        
        psi =  psi + Psi_dot *t_setp
        x +=  -v *np.sin(psi) * t_setp
        y +=  v* np.cos(psi) * t_setp
        
        # x = x + -v *np.sin(psi) *dt
        # y = y + v* np.cos(psi) *dt
        # x = -v *np.sin(psi) *t_setp
        # y = v* np.cos(psi) *dt
        
        xlist = np.append(xlist,x)
        ylist = np.append(ylist,y)
        
    all_x = np.append(all_x,xlist)
    all_y = np.append(all_y,ylist)
    
    
    ax.plot(xlist, ylist,'o')
    # plt.grid()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

# lgd = ax1.legend([ 'Lag ' + str(lag.size) for lag in all_x])
# lgd = ax2.legend()
# plt.ioff()
plt.show()
