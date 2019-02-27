# 17 January 2019 - 20 January 2019
'''
LET'S GET DOWN TO Bismuth ;)

1. Create the matrix 
	Dimension: n x m
	M --> for the scores
	P --> for the pointers
2. Initialise
	First cell = 0
	First row: starting from zero, 
		for each position add the gap penalty to the previous cell's score
	First column: starting from zero, 
		for each position add the gap penalty to the previous cell's score
3. Populate the matrix	
	Begin at cell (1,1)
	For each cell in the matrix compute:
		side = score_to_the_left + gap_penalty
		diag = score_on_the_diagonal + substitution_score
		down = score_above + gap_penalty
	Then select the maximum of the three:
		In the M cell --> store the score 
		In the P cell --> store 0 if the MAX score is side
								1 if the MAX score is diag
								2 if the MAX score is down		
4. Trace-back
	Begin at cell (m,n) of P
	Read content of cell (m,n)
	Initialise aligned sequences 1 & 2
	Until cell (0,0) is reached:
		If cell is: 0 --> add letter n-1 to al1 and - to al2
					1 --> add letter n-1 to al1 and letter m-1 to al2
					2 --> add - al1 and letter m-1 to al2
		If cell is: 0 --> add to current position (0,-1)
					1 --> add to current position (-1,-1)
					2 --> add to current position (-1,0)
		Read current position's cell content
5. Compute the score and return alignment
'''
# Produces an empty matrix of dimension col x row
def make_matrix(col,row):
	matrix = [['*' for col in range(col)] for row in range(row)]
	return matrix

# Sum of two vectors, v represented by lists
def v_sum(l1,l2):
	res = []
	for i in range(len(l1)):
		res.append(l1[i]+l2[i])
	return res

def prettyMatrix(M):
	for row in M:
		i=''
		for el in row:
			i=i+str(el)+'\t'
		print(i,'\n')
	print('dimensions --> %dx%d\n'%(len(row),len(M)))
	
# Prints the alignment of two sequences in a readable way
def prettyAlignment(al1, al2):
	# Given 2 sequences of equal length creates a string of | 
	# to mark the matching positions
	try:
		match = ''
		for i in range(len(al1)):
			if al1[i] == al2[i]:
				match = match + '|'
			else:
				match = match + ' '
		# Every 80 chracters prints the 1st sequence, match and 2nd sequence
		e = 0
		for e in range(80,len(al1),80):
			print('',al1[e-80:e],'\n',match[e-80:e],'\n',al2[e-80:e],'\n')
		print('',al1[e:],'\n',match[e:],'\n',al2[e:])
		
	except:
		print('These two sequences are not aligned, the alignment cannot be printed')
	
	
# Returns the MAX of a list and its position inside the list
def max_list_position(l):
	m = l[0]
	position = 0
	for i in range(len(l)):
		if l[i]>m:              # What if they are the same???
			m=l[i]
			position = i
	return [m,position]

# Computes the value for (I,J) of the score matrix and its pointer
# 	put here the scoring parameters? Should they be a parameter for the function?
def fill_in(I,J):
	# Scoring parameters of the alignment
	score = [[ 2,-1,-1, 0], [-1, 2, 0,-1], [-1, 0, 2,-1], [0,-1, -1, 2]] # Subsitution matrix
	conv = {'A':0,'C':1,'T':2,'G':3}  # Converts the indexes of the substitution matrix into Bases
	d = -2
	# Compute the three possibilities
	side = (M[J][I-1]) + d  # Score to the left + gap
	diag = (M[J-1][I-1]) + (score[conv[sq1[I-1]]][conv[sq2[J-1]]])  # diagonal score + substitution score  | the (-1) matches the matrix index to the sequences
	down = (M[J-1][I]) + d  # score above + gap
	# Select max alignment score and related pointer {0:side,1:diag,2:down}
	res = max_list_position([side,diag,down]) 
	return res



### INITIAL INPUT
d = -2
# The sequences sq1 --> n  sq2 --> m
sq1 = 'GTACCCATG'#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
sq2 = 'ACCA'#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
n = len(sq1)
m = len(sq2)
print(sq1, sq2,'\n')


########  INITIALIZE THE MATRIX  ########  
# Make the score matrix and the pointer matrix
M = make_matrix(n+1,m+1) 
P = make_matrix(n+1,m+1) 
# Initialise the first row: M --> gap penalty |  P --> row of 0  
M[0] = [ d*i for i in range(n+1)]
P[0] = [ 0 for i in range(n+1)]
# Initialise the first column: M --> gap penalty |  P --> column of 2 
for i in range(1,m+1):
	M[i][0] = d*i
	P[i][0] = 2

########  POPULATE THE MATRIX  ########  
# column --> i  
# row --> j
for j in range(1,m+1):
	for i in range(1,n+1):
		result = fill_in(i,j)
		M[j][i] = result[0]
		P[j][i] = result[1]
#~ prettyMatrix(M)
#~ prettyMatrix(P)

########  TRACE-BACK  ########  
# Begin traceback at cell (m,n) of matrix P
s = [m,n]  # position in P
cell = P[s[0]][s[1]]   # content in cell in P(s)
# Initialise the new aligned sequences
al1 = '' 
al2 = ''
# Traceback following the pointers in P until position (0,0) is reached,
# while building the alignment step-wise
while s != [0,0]:
	# Build the alignment at position s
	align = {0:[sq1[s[1]-1],'-'],
			1:[sq1[s[1]-1],sq2[s[0]-1]],
			2:['-',sq2[s[0]-1]]}
	al1 = al1 + align[cell][0]
	al2 = al2 + align[cell][1]
	# Move to next positon following the pointer
	move = {0:[0,-1],1:[-1,-1],2:[-1,0]}  # pointer direction conversion
	s = v_sum(s,move[cell])
	# Read new position's cell content
	cell = P[s[0]][s[1]]
	#~ print('>>',s,cell,'\n',al1,'\n',al2)
	
########  ALIGNMENT & SCORE   ######## 
prettyAlignment(al1[::-1],al2[::-1])
print('\nThe alignment score is %d' %M[m][n])

'''
redo using just the 0,1,2 P matrix 
to each number must correspond a sliding behaviour and a way to grab the letters from the sequence 
{0:[0,-1],1:[-1,-1],2:[-1,0]}
the corresponding list can be summed to the slider

{0:['-',slider[1]],1:[slider],2:[slider[0],'-']}
then we use the coohordinates of this dictionary to either add a gap or as a index to the sequence
'''
