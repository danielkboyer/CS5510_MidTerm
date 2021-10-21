from matplotlib import pyplot as plt
import numpy as np
from numpy.core.fromnumeric import var
from numpy.core.numeric import Infinity
from p5_b_hyperparameter_tuning import tune
from utils import find_inverse_kinematics, dist, ts, ds
ACTUATOR_RADIUS = 0.05
# ALPHA = 17.91
ALPHA = 1000
def d_theta(arc_len):
	return arc_len / ACTUATOR_RADIUS

def get_config_cost_p6(vars, original_configuration):
	c = 0
	c += 2 * d_theta(np.absolute(original_configuration[0] - vars[0])) # t1 cost 3x the energy
	for index in ds:
		c += d_theta(np.absolute(original_configuration[index] - vars[index]))
	for index in ts:
		c += 2 * np.absolute(vars[index] - original_configuration[index]) # d1,d2 cost 2x the energy
	return c
def cost_p6(p1, p2, currVariables, plot, ALPHA, ay_axis, ax_axis, original_configuration):
	new_vars_cost = get_config_cost_p6(currVariables, original_configuration)
	# print(new_vars_cost)
	if (new_vars_cost > ALPHA):
		 return np.Infinity
	if plot:
		ay_axis.append(new_vars_cost / len(currVariables))
		ax_axis.append(ax_axis[-1] + 1)
	return dist(p1,p2)

tune(cost_p6, 230, 245, 5, 2)