
import numpy as np
from utils import find_inverse_kinematics

goal = np.array((1.2, 0.8, 0.5))
t1 = np.radians(-90)
d2 = 0.5
d3 = 1.0
t4 = np.radians(-90)
t5 = np.radians(90)
t6 = np.radians(40)

variables = np.array([
	t1, #t1
	d2, #d2
	d3, #d3
	t4, #t4
	t5, #t5
	t6  #t6
])
find_inverse_kinematics(goal, variables, 40000)