import numpy as np
from matplotlib import pyplot as plt
from itertools import permutations
from utils import find_inverse_kinematics, get_T_matrix, dist
from p5_b_hyperparameter_tuning import get_config_cost

def total_distance(start, positions):
	d = dist(start, positions[0])
	for pos in range(len(positions)-1):
		print(pos)
		d += dist(positions[pos], positions[pos+1])
	return d


def find_shortest_path(startPos, goals):
	perms = list(permutations(goals))
	best = perms[0]
	best_distance = np.Infinity 
	for perm in perms:
		new_distance = total_distance(startPos, perm)
		if new_distance < best_distance:
			best_distance = new_distance
			best = perm
	return best	


tot = 0
def cost(p1, p2, currVariables, plot, ALPHA, ay_axis, ax_axis, original_configuration, tot=None):
	new_vars_cost = get_config_cost(currVariables, original_configuration)
	if tot: tot += new_vars_cost
	if plot:
		ay_axis.append(new_vars_cost)
		ax_axis.append(ax_axis[-1] + 1)
	return dist(p1,p2)


goals = np.array([
	np.array([1,1,1]),
	np.array([-1,1,1])
])
variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) # t1, d2, d3, t4, t5, t6
newT = get_T_matrix(variables)
newPos =  np.array((newT[0,3], newT[1,3], newT[2,3]))
best = find_shortest_path(newPos, goals)

ay_axis=[0]
ax_axis=[0]
kin_data = find_inverse_kinematics(best[1], variables, 10000, cost=cost, original_configuration=[i for i in variables], get_total_cost=get_config_cost, ay_axis=ay_axis, ax_axis=ax_axis)
first_move = kin_data[3]
total_dist = kin_data[4]


print(first_move)
print('total cost', kin_data[4])


