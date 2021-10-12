import numpy as np


ts = [0,3,4,5]
ds = [1,2]
vs = [0,0,0,0,0]
d0 = 1
d5 = 1.1

def c(index):
	return np.cos(vs[ts[index]])

def s(index):
	return np.sin(vs[ts[index]])

def d(index):
	return ds[index]


r11 = c(0)*c(3)*c(4)*c(5) - c(0)*s(3)*s(5) + s(0)*s(4)*c(5)
r21 = s(0)*c(3)*c(4)*c(5) - s(0)*s(3)*s(5) - c(0)*s(4)*s(5)
r31 = -s(3)*c(4)*c(5) - c(3)*s(5)
r12 = -s(0)*c(3)*c(4)*s(5) - c(0)*s(3)*c(5) - s(0)*s(4)*c(5)
r22 = -s(0)*c(3)*c(4)*s(5) - s(0)*s(3)*c(5) + c(0)*s(4)*c(5)
r32 = s(3)*c(4)*c(5) - c(3)*c(5)
r13 = c(0)*c(3)*s(4) - s(0)*c(4)
r23 = s(0)*c(3)*s(5) + c(0)*c(4)
r33 = -s(3)*s(4)
dx = c(0)*c(3)*s(4)*d(1) -s(0)*c(4)*d(1) - s(0)*d(0)
dy = s(0)*c(3)*s(5)*d(1) + c(0)*c(4)*d(1) + c(0)*d(1)
dz = -s(3)*s(4)*d(1) + d0 + d(1)
