# 5 March 2019
# Functions for the sequence algorithms

# Creates a matrix with dimension row x col
def make_matrix(row,col):
	M = [['*' for j in range(col)] for i in range(row)]
	return M
#~ print(make_matrix(4,6))

# Prints a matrix in a readable way
def print_matrix(M):
	for row in M:
		line = ''
		for el in row:
			if type(el) == float:
				line += '{:.2e}'.format(el) +'\t'
			else: 
				line += str(el) + '\t' 
		print(line,'\n')
	print('dimensions --> %dx%d\n'%(len(row),len(M)))
#~ print_matrix(make_matrix(4,6))

# Returns the MAX of a list and its position inside the list
def max_list_position(l):
	max_val = l[0]
	pos = 0
	for i in range(len(l)):
		if l[i]> max_val:
			max_val = l[i]
			pos = i
	return [max_val,pos]

# Prints the alignment of two sequences in a readable way
def print_alignment(sq1,sq2):
	try:
		sym = ''
		for k in range(len(sq1)):
			if sq1[k] == sq2[k]:
				sym = sym + '|'
			else:
				sym = sym + ' '
		e = 0
		for e in range(80,len(sq1),80):
			print("%s\n%s\n%s"%(sq1[e:e+80],sym[e:e+80],sq2[e:e+80]))
		print("%s\n%s\n%s"%(sq1[e:],sym[e:],sq2[e:]))
	except:
		print('sequences not correctly aligned')
#~ print_alignment('AATGGTT','AATTGGC')
			
