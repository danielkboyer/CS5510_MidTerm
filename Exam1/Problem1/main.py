

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np




def GetExactCoord(t):
    x_exact = R * np.cos(2*np.pi*t/2.173) + -R
    y_exact = -R * np.sin(2*np.pi*t/2.173)

    return (x_exact,y_exact)
   
    
def GetMagnitude(x,y,x_2,y_2):
    return np.sqrt((x_2 - x)*(x_2 - x) + (y_2 - y)*(y_2 - y))

v= 20
colors = ['r', 'g', 'b', 'm', 'y']
LINEWIDTH=0.8
t_list = [.01, 0.1, 1]
max_time =10

L = 4
alpha = -np.pi/6
R = 4/np.tan(alpha)
V = 20
Psi_dot = (V * np.tan(alpha)) / L

all_x =[]
all_y =[]
fig = plt.figure()
ax = fig.add_subplot(121)
ax_2 = fig.add_subplot(122)
for i, t_setp in enumerate(t_list):
    # t = np.arange(0.0, t_setp, max_time)
    x = 0 
    y = 0
    psi = 0 
    xlist =[]
    ylist =[]

    x_help_list = []
    y_help_list = []
    x_error_list =[]
    y_error_list = []
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

        
        x_error_list = np.append(x_error_list,dt)
        exact_coords = GetExactCoord(dt)

        x_help_list = np.append(x_help_list,exact_coords[0])
        y_help_list = np.append(y_help_list,exact_coords[1])
        y_error_list = np.append(y_error_list,GetMagnitude(x,y,exact_coords[0],exact_coords[1]))
        
    all_x = np.append(all_x,xlist)
    all_y = np.append(all_y,ylist)
    
    
    if i ==0:
        ax.plot(x_help_list, y_help_list, 'c', label='continuous',  linewidth=LINEWIDTH)
    ax.plot(xlist, ylist, colors[i], label=f'dt={t_setp}', linewidth=LINEWIDTH)
    ax_2.plot(x_error_list,y_error_list, colors[i], linewidth=LINEWIDTH)
    ax.legend()
    # plt.grid()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

# lgd = ax1.legend([ 'Lag ' + str(lag.size) for lag in all_x])
# lgd = ax2.legend()
# plt.ioff()
plt.show()
plt.savefig('plot.png')


