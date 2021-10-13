import numpy as np

def get_h_matrix(theta, length):
    c = np.cos(theta)
    s = np.sin(theta)
    mt =  np.matrix([
        [c, -s, 0, length*c],
        [s,  c, 0, length*s],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
        ])
    return mt

a0 = get_h_matrix(np.pi/6, 0.6)
a1 = get_h_matrix(np.pi/4, 0.4)
print("T = %s" % np.matmul(a0, a1))