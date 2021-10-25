

from matplotlib import pyplot as plt
import numpy as np
from utils import find_inverse_kinematics
from p5_b_hyperparameter_tuning import cost as p5_cost, BEST_ALPHA

def main():
	goal = np.array((1.2, 0.8, 0.5))
	variables = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
	original_configuration = np.array([i for i in variables])
	ax_axis = [0]
	ay_axis = [0]
	kin_data = find_inverse_kinematics(goal, variables, 100000, cost=p5_cost, ALPHA=BEST_ALPHA, ay_axis=ay_axis, ax_axis=ax_axis, original_configuration=original_configuration)
	fg, ax1 = plt.subplots()
	ax1.plot(kin_data[0][0], kin_data[0][1], linewidth=1)

	ax1.set_xlabel('trial #')
	ax1.set_ylabel('distance to goal')
	plt.show()


if __name__ == "__main__":
	main()