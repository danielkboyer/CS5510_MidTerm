from matplotlib import pyplot as plt
import numpy as np
from numpy.core.fromnumeric import var
from numpy.core.numeric import Infinity
from utils import find_inverse_kinematics, dist, ts, ds
BEST_ALPHA = 17.91
ACTUATOR_RADIUS = 0.05
ACCAPTED_DISTANCE = 0.01
def d_theta(arc_len):
	return arc_len / ACTUATOR_RADIUS

def get_config_cost(vars, original_configuration):
	c = 0
	for index in ds:
		c += d_theta(np.absolute(original_configuration[index] - vars[index]))
	for index in ts:
		c += np.absolute(vars[index] - original_configuration[index])
	return c
def cost(p1, p2, currVariables, plot, ALPHA, ay_axis, ax_axis, original_configuration):
	new_vars_cost = get_config_cost(currVariables, original_configuration)
	if (new_vars_cost > ALPHA):
		 return np.Infinity
	if plot:
		ay_axis.append(new_vars_cost)
		ax_axis.append(ax_axis[-1] + 1)
	return dist(p1,p2)
def main():
	n = 15
	m = 20
	step = 0.15 
	trials = 20 
	bests = {}
	for i in range(trials):
		print('i', i)
		best_a = n
		best_a_score = np.Infinity
		for ALPHA in np.arange(n,m,step):

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
			original_configuration = np.array([i for i in variables])
			ax_axis = [0]
			ay_axis = [0]

			kin_data = find_inverse_kinematics(goal, variables, 10000, cost=cost, ALPHA=ALPHA, ay_axis=ay_axis, ax_axis=ax_axis, original_configuration=original_configuration)

			if kin_data[1] < ACCAPTED_DISTANCE and ay_axis[-1] < best_a_score:
				best_a = ALPHA
				best_a_score = ay_axis[-1]
		if best_a in bests:
			bests[best_a] += 1
		else:
			bests[best_a] = 1
	weighted_avg_alpha = 0
	for i in bests:
		weighted_avg_alpha += i * bests[i]
	weighted_avg_alpha /= trials
	print(bests)
	print("The optimal alpha value is: %f" % weighted_avg_alpha)

if __name__ == "__main__":
	main()