from matplotlib import pyplot as plt
import numpy as np
from numpy.core.fromnumeric import var
from numpy.core.numeric import Infinity
from utils import find_inverse_kinematics, dist, ts, ds
BEST_ALPHA = 17.91
def d_theta(arc_len):
	return arc_len / ACTUATOR_RADIUS

def get_config_cost(vars):
	c = 0
	for index in ds:
		c += d_theta(np.absolute(original_configuration[index] - vars[index]))
	for index in ts:
		c += np.absolute(vars[index] - original_configuration[index])
	return c
def cost(p1, p2, currVariables, plot ):
	new_vars_cost = get_config_cost(currVariables)
	if (new_vars_cost > ALPHA):
		 return np.Infinity
	if plot:
		y_axis.append(new_vars_cost)
		x_axis.append(x_axis[-1] + 1)
	return dist(p1,p2)

fig, (ax1, ax2) = plt.subplots(1, 2)
n = 15
m = 20
step = 0.15
bests = {}
for i in range(20):
	print('i', i)
	best_a = n
	best_a_score = np.Infinity
	# for ALPHA in range(n,m):
	for ALPHA in np.arange(n,m,step):

		ACTUATOR_RADIUS = 0.05
		ACCAPTED_DISTANCE = 0.01
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
		x_axis = [0]
		y_axis = [0]


		kin_data = find_inverse_kinematics(goal, variables, 10000, cost=cost)
		# ax1.plot(kin_data[0][0], kin_data[0][1], linewidth=1, label="%d"%ALPHA)
		print("Final combined distance traveled for each part: %.2f radians (%.2f radians per component)" % (y_axis[-1], y_axis[-1] / len(variables)))
		# ax2.plot(x_axis, y_axis, linewidth=1)

		if kin_data[1] < ACCAPTED_DISTANCE and y_axis[-1] < best_a_score:
			best_a = ALPHA
			best_a_score = y_axis[-1]
	if best_a in bests:
		bests[best_a] += 1
	else:
		bests[best_a] = 1
print("best alpha: %2d" % best_a)
print(bests)
ax1.legend()
# plt.show()
