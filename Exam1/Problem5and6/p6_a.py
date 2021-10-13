
import numpy as np
from numpy.core.fromnumeric import var
from utils import find_inverse_kinematics

goal = np.array((1.2, 0.8, 0.5))
variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) # t1, d2, d3, t4, t5, t6
def cost(p1, p2, curr_variables, new_variables):
	return 1

find_inverse_kinematics(goal, variables, 4000)