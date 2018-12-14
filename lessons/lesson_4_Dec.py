#distance of two points
from math import sqrt 

def distance_2_points(a,b):
	x1= a[0]
	x2= b[0]
	y1= a[1]
	y2= b[1]
	return sqrt((pow((x1-x2),2))+(pow((y1-y2),2)))
#~ A=[float(input('Enter coordinate A1: ')),float(input('Enter coordinate A2: '))]
#~ B=[float(input('Enter coordinate B1: ')),float(input('Enter coordinate B2: '))]
#~ print('The distance between A and B is %f'%distance_2_points(A,B))

def roots(x):
	a=x[0]
	b=x[1]
	c=x[2]
	delta=sqrt(pow(b,2)-4*a*c)
	return (((-b-delta)/(2*a)),((-b+delta)/(2*a)))
	
	
#~ print('The roots are ',roots([1,0,-1]))

def roots_of_equation(a, b, c):
    '''Input: the three parameters a, b, c; Output: the roots
       of a 2nd degree equation'''
   
    from math import sqrt

    a = float(a)
    b = float(b)
    c = float(c)

    root1 = - b - sqrt(b**2 - 4*a*c)/2*a
    root2 = - b + sqrt(b**2 - 4*a*c)/2*a

    return float(root1), float(root2)

def test_roots_of_equation():
    '''This function is meant to test the functioning of another function
       i.e., roots_of_equation(). Input is not required, Output: a string
       to be printed'''

    a = input("type the first parameter of a 2nd degree equation: ")
    b = input("type the second parameter of a 2nd degree equation: ")
    c = input("type the third parameter of a 2nd degree equation: ")

    roots = roots_of_equation(a, b, c)

    return "x0 = {0:3.1f}, x1 = {1:3.1f}".format(roots[0],roots[1])

print(test_roots_of_equation())


