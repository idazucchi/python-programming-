# March 7th, 2019 - Ida Zucchi

# Given a list returns the maximum value of the list and its position in it
def max_list_position(l):
	max_val = l[0]
	pos = 0
	for e in range(len(l)):
		if l[e]>max_val:
			max_val = l[e]
			pos = e
	return [max_val,pos]

# Given a matrix prints its contents row by row, separating the elements with tabs
def print_matrix(M):
	for row in M:
		line = ''
		for el in row:
			line = line + str(el) + '\t'
		print("%s\n"%line)

# Given 2 sequences, a gap penalty, a substitution matrix and a dictionary to convert the characters
# of the sequences into indeces, computes the Score and Pointer matrices for the NW algorithm
def Needelman_Wunsch(sq1,sq2,d,subst_m,subst_i):
	# Create the Score and Pointer matrices
	S = [['*' for j in range(len(sq1)+1)] for i in range(len(sq2)+1)]
	P = [['*' for j in range(len(sq1)+1)] for i in range(len(sq2)+1)]
	# Initialise the first row
	S[0] = [j*d for j in range(len(sq1)+1)]
	P[0] = ["\u2190" for j in range(len(sq1)+1)]
	P[0][0] = '*'
	# Initialise the first column
	for i in range(1,len(sq2)+1):
		S[i][0] = i*d
		P[i][0] = "\u2191"
	# Fill in the matrices row by row, left to right. Begin at position (1,1)
	for i in range(1,len(sq2)+1):
		sq2_char = sq2[i-1]
		for j in range(1,len(sq1)+1):
			sq1_char = sq1[j-1]
			# Compute the score for the cell coming from the left, up or diagonal
			side = S[i][j-1] +d
			diag = S[i-1][j-1] + subst_m[subst_i[sq2_char]][subst_i[sq1_char]]
			down = S[i][j-1] +d
			# Pick the best score
			max_score = max_list_position([side,diag,down])
			# Store best score and its position
			S[i][j] = max_score[0]
			arrow = {0:"\u2190",1:"\u2196",2:"\u2191"}
			P[i][j] = arrow[max_score[1]]
	return [S,P]


if __name__ == '__main__':
	# Initial input
	seqA = 'ACTGC'
	seqB = 'ATCC'
	D = -2
	substitution_m = [[2,-1,-1,0],
					  [-1,2,0,-1],
					  [-1,0,2,-1],
					  [0,-1,-1,2]]
	substitution_i = {'A':0,'C':1,'T':2,'G':3}
	# Compute the Score and Pointers matrices
	matrices = Needelman_Wunsch(seqA,seqB,D,substitution_m,substitution_i)
	Score = matrices[0]
	Pointers = matrices[1]
	print("Score matrix")
	print_matrix(Score)
	print("Pointers matrix")
	print_matrix(Pointers)
		
		
