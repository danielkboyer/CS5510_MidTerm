
import math
gravity = 9.8
total_mass = 2
length = 0.5
masspole = 0.1
masscart = 1
polemass_length = masspole * length
total_mass = masspole + masscart

def eqs(theta, theta_dot):
	costheta = math.cos(theta)
	sintheta = math.sin(theta)
	force = 0
	temp = ( force + polemass_length * theta_dot ** 2 * sintheta) / total_mass
	thetaacc = (gravity * sintheta - costheta * temp) / (
	length * (4.0 / 3.0 - masspole * costheta ** 2 / total_mass)
	)
	xacc = temp - polemass_length * thetaacc * costheta / total_mass

	return thetaacc, xacc

