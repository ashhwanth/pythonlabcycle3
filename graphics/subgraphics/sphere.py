from math import pi

def spherearea():
	r = float(input('Radius of sphere: '))
	sur_area = 4 * pi * r **2
	volume = (4/3) * (pi * r ** 3)
	print("Surface Area is: ", sur_area)
	print("Volume is: ", volume)
#spherearea()
