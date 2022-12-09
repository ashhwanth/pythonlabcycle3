from math import pi

def area_peri_circle():
	r = float(input("Enter radius of the circle: "))
	area = (pi*r*r)
	perimeter = (2*pi*r)
	print("The area of circle is ", "%.2f" %area)
	print("The perimeter of circle is", "%.2f" %perimeter)
#area_peri_circle()
