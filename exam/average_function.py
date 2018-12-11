# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
prepare empty list v
repeat 10 times the following actions:
	enter a value from the keyboard
	add it to v
prepare empty variable tot
repeat 10 times the following action:
	add to tot the value of v corresponding to the number of the repetition
compute the mean as tot divided by the number of elements in v (which is 10)
print to screen v and mean
'''

def make_vector(n):
	v=[]
	for i in range(n):
		value=float(input('enter the %i value for the vector: '%i))
		v.append(value)
	return v
		
def vector_mean_10(v):
	if len(v)!=10:
		return print('cannot compute mean, vector size must be 10')
	else:
		tot=0
		for el in v:
			tot=tot+el
		mean=tot/10
		return [v,mean]
		
V=make_vector(10)
print(type(V))
print('the mean of the vector ',V,' is %.1f'%vector_mean_10(V)[1])
