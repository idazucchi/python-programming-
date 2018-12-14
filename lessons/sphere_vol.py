#Code to compute the volume of a sphere from its diamter & prints it (applicated to a cell)
from math import pi, pow

d=float(input('Enter the diameter of the cell \n'))
#input_file
in_filef=open('diameter.txt') #print returns <_io.TextIOWrapper name='diameter.txt' mode='r' encoding='UTF-8'>
r=d/2
V=4/3*pi*pow(r,3)
V=round(V,3)
print('The volume of the cell, assuming it is spherical, is %f' %V )

with open("mew1.txt", "r") as myFile:
	myFile.write("0_0")
	
print("smth")
