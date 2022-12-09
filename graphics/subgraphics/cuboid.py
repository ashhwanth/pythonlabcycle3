def cuboidarea():
	l=float(input('Please Enter the Length of a Cuboid: '))
	w=float(input('Please Enter the Width of a Cuboid: '))
	h=float(input('Please Enter the Height of a Cuboid: '))
	SA=2*(l*w+l*h+w*h)
	p=4*(l+w+h)
	print("Surface area of Cuboid : ",SA)
	print("Perimeter of Cuboid : ",p)
#cuboidarea()
