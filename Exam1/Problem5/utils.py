import numpy as np
beginning = 1.1 #d1
end = 1.2 #d6
ts = np.array([0, 3, 4, 5])
ds = np.array([1, 2])
# variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) # t1, d2, d3, t4, t5, t6

def random_step(curr_variables, quench=1):
	new_variables = np.array([i for i in curr_variables])
	for index in ts:
		new_variables[index] += np.pi * 2 * (np.random.rand() - 0.5) * 2

	for index in ds:
		new_variables[index] += (np.random.rand() - 0.5) * 0.05 * quench

	return new_variables


def cost(p1, p2): # distance between points
	return np.linalg.norm(p1 - p2)

def get_T_matrix(variables):
	def c(index):
		return np.cos(variables[index-1])

	def s(index):
		return np.sin(variables[index-1])

	def d(index):
		return variables[index-1]
	r11 = c(1)*c(4)*c(5)*c(6) - c(1)*s(4)*s(6) + s(1)*s(5)*c(6)
	r21 = s(1)*c(4)*c(5)*c(6) - s(1)*s(4)*s(6) - c(1)*s(5)*s(6)
	r31 = -s(4)*c(5)*c(6) - c(4)*s(6)
	r12 = -s(1)*c(4)*c(5)*s(6) - c(1)*s(4)*c(6) - s(1)*s(5)*c(6)
	r22 = -s(1)*c(4)*c(5)*s(6) - s(1)*s(4)*c(6) + c(1)*s(5)*c(6)
	r32 = s(4)*c(5)*c(6) - c(4)*c(6)
	r13 = c(1)*c(4)*s(5) - s(1)*c(5)
	r23 = s(1)*c(4)*s(6) + c(1)*c(5)
	r33 = -s(4)*s(5)
	dx = c(1)*c(4)*s(5)*d(2) -s(1)*c(5)*end - s(1)*d(1)
	dy = s(1)*c(4)*s(6)*d(2) + c(1)*c(5)*end + c(1)*d(2)
	dz = -s(4)*s(5)*end + beginning + d(2)

	T = np.matrix([
		[r11, r12, r13, dx],
		[r21, r22, r23, dy],
		[r31, r32, r33, dz],
		[  0,   0,   0,  1]
	])
	return T



def find_inverse_kinematics(goal, variables, iterations):
	for i in range(1,iterations):

		currT = get_T_matrix(variables)
		currPos = np.array((currT[0,3], currT[1,3], currT[2,3]))

		newVars = random_step(variables, quench=1 - (i * 1/iterations))
		newT = get_T_matrix(newVars)
		newPos =  np.array((newT[0,3], newT[1,3], newT[2,3]))

		if cost(currPos, goal) > cost(newPos, goal):
			print("%d: %.2f" % (i, cost(newPos, goal)))
			variables = newVars


	currT = get_T_matrix(variables)
	currPos = np.array((currT[0,3], currT[1,3], currT[2,3]))
	print("goal:", goal)
	print("final position:", currPos)
	print("distance to goal: %.5f m" % cost(currPos, goal))
	for i, j in enumerate(ts):
		print("theta %d: %.5f rad" % (j+1, variables[j]))
	print("d%d: %.5f m" % (1, beginning))
	for i, j in enumerate(ds):
		print("d%d: %.5f m" % (j+1, variables[j]))
	print("d%d: %.5f m" % (6, end))

