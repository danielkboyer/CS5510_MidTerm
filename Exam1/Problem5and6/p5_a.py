import numpy as np
from matplotlib import pyplot as plt
from utils import find_inverse_kinematics

goal = np.array((1.2, 0.8, 0.5))
variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) # t1, d2, d3, t4, t5, t6
ay_axis = [0]
ax_axis = [0]
kin_data = find_inverse_kinematics(goal, variables, 10000, ALPHA=None, ay_axis=ay_axis, ax_axis=ax_axis, original_configuration=[i for i in variables])

fg, ax1 = plt.subplots()
ax1.plot(kin_data[0][0], kin_data[0][1], linewidth=1)

ax1.set_xlabel('trial #')
ax1.set_ylabel('distance to goal')
plt.show()