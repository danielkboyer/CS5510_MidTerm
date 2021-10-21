
from matplotlib import pyplot as plt
import numpy as np
from utils import find_inverse_kinematics
from p5_b_hyperparameter_tuning import cost as p5_cost
BEST_ALPHA = 17.91 # this was calculated in p5_b_hyperparameter_tuning.py
def main():

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

	find_inverse_kinematics(goal, variables, 10000, cost=p5_cost, ALPHA=BEST_ALPHA, ay_axis=ay_axis, ax_axis=ax_axis, original_configuration=original_configuration)


if __name__ == "__main__":
	main()