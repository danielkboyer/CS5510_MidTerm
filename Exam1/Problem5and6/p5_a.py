import numpy as np
from utils import find_inverse_kinematics

goal = np.array((1.2, 0.8, 0.5))
variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) # t1, d2, d3, t4, t5, t6
find_inverse_kinematics(goal, variables, 10000)