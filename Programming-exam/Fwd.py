# 17 January 2019 - 20 January 2019
'''
LET'S GET DOWN TO Bismuth ;)

	Forward algorithm for HMM
Compute the p of a given sequence given a certain model

1. Create the matrix 
	Dimension: n+2 x m
	P --> probability
2. Initialise
	First cell = 1
	First column: starting from row = 1 --> each cell = 0
3. Iteration	
	Begin at cell (0,1)
	Column by column, for each cell in the matrix compute:
		For each cell in the previous column:
			g = the probability in the cell * the transition probability
		sum all the g	
		multilpy it by the emission probability for that cell
4. Termination
	For each cell of the last column compute:
		For each cell in the previous column:
			g = the probability in the cell * the transition probability
		sum all the g	 
5. The desired result is in the last cell of the last column
'''
# Produces an empty matrix of dimension col x row
def make_matrix(col,row):
	matrix = [['*' for col in range(col)] for row in range(row)]
	return matrix

# Prints a list of lists as a legible matrix
def prettyMatrix(M):
	for row in M:
		i=''
		for el in row:
			i=i+str(el)+'\t'
		print(i,'\n')
	# Prints the dimensions
	print('dimensions --> %dx%d\n'%(len(row),len(M)))
	
# Computes the emission propability of the character seq(j) from state i 	
def emission_prob(i,j):
	row = i
	col = h_emission_index[seq[j]]
	return emission[i][col]

# Compute the probability for the sequence up to seq(j) to be generated 
# by a path ending in the state i, minus the emission probility factor
def fill_in(i,j): 
	res = 0
	# Compute the sum over all the states
	for k in range(len(states)):
		# Compute the p of transitioning from state k to i 
		contribute = (P[k][j-1]) * transitions_prob[k][i]  #multiply by transition
		#~ print(contribute, type(contribute),'--<', i, j)
		#~ print(transitions_prob[k][i])
		res = res + contribute
	return res


### INITIAL INPUT
seq = 'ATGCG'
# HMM Model
states = ['b','Y','N','e']
# Transition probabilities [states x states]
transitions_prob =  [[0,0.2,0.8,0],
					[0,0.7,0.2,0.1],
					[0,0.1,0.8,0.1],
					[0,0,0,0]]
# Transition probabilities index
states_index = {'b':0,'Y':1,'N':2,'e':3}
# Emission probabilities [states x characters]
emission = [[0.0, 0.0, 0.0, 0.0],
			[0.1, 0.4, 0.4, 0.1],
			[0.25,0.25,0.25,0.25],
			[0.0, 0.0, 0.0, 0.0]]
# Emission probabilities horizontal index
h_emission_index = {'A':0,'G':1,'C':2,'T':3}

########  INITIALIZE THE MATRIX  ########  
# Make the matrix
P = make_matrix(len(seq)+2,4)
# Match the sequence index to P --> add empty char to front and back seq
seq = '-' + seq + '-'
print(seq) 
# Initialise cell (0,0) 
P[0][0] = 1
# Initialise the first column
for i in range(1,len(states)):
	P[i][0] = 0
#~ prettyMatrix(P)

########  		ITERATION 		 ######## 
# Fill the matrix column by column
for j in range(1,len(seq)-1):
	for i in range(0,len(states)):
		# Compute the p of the sequence up to seq(j) in state i
		P[i][j] = round(fill_in(i,j) * emission_prob(i,j),5 )   #multiply by emission

########  		TERMINATION 		 ######## 
# Fill in the last column
for i in range(0,len(states)):
	# Compute the p of the sequence up to seq(j) in state i
	P[i][len(seq)-1] = '{:.2e}'.format(fill_in(i,len(seq)-1))

########  		RESULTS		 ######## 
# Print the probability matrix
prettyMatrix(P)
# Print result
print('Given the current model the probability of the sequence %s\n is %s'%(seq[1:len(seq)-1],P[i][len(seq)-1]))







	
