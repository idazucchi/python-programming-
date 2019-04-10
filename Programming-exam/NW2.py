# 5 March 2019
# Needelman and Wunsch but more modularized
import gems as g

def Needelman_Wunsch_M(sq1,sq2,D,subst_m,subst_i):
	# Create Score matrix and Pointer matrix
	S = g.make_matrix(len(sq2)+1,len(sq1)+1)
	P = g.make_matrix(len(sq2)+1,len(sq1)+1)
	# Initialise the first row and column
	for j in range(len(sq1)+1):
		S[0][j] = D * j
		P[0][j] = 0
	for i in range(1,len(sq2)+1):
		S[i][0] = D * i
		P[i][0] = 2
	# Populate the matrices
	for i in range(1,len(sq2)+1):
		for j in range(1,len(sq1)+1):
			#~ res = fill_in(i,j,sq1,sq2,D,subst_m,subst_index)
			side = S[i][j-1] + D
			diag = S[i-1][j-1] + subst_m[subst_i[sq1[j-1]]][subst_i[sq2[i-1]]]
			down = S[i-1][j] + D
			res = g.max_list_position([side,diag,down])
			S[i][j] = res[0]
			P[i][j] = res[1]
	return [S,P]

def Traceback(start,stop,sq1,sq2,P):
	I = start[0]
	J = start[1]
	al1 = ''
	al2 = ''
	while (I!=stop[0]) and (J!=stop[1]):
		cell = P[I][J]
		align = {0:[sq1[J-1],'-'],
				 1:[sq1[J-1],sq2[I-1]],
				 2:['-',sq2[I-1]]}
		al1 = al1 + align[cell][0]
		al2 = al2 + align[cell][1]
		move = {0:[-1,0], 1:[-1,-1], 2:[0,-1]}
		J = J + move[cell][0]
		I = I + move[cell][1]
	return [al1[::-1],al2[::-1]]


if __name__ == '__main__':
	# INITIAL INPUT
	seq1 = 'ACTGC'
	seq2 = 'ATCC'
	substitution_m = [[ 2,-1,-1, 0],
					  [-1, 2, 0,-1], 
					  [-1, 0, 2,-1], 
					  [0,-1, -1, 2]]
	substitution_index = {'A':0,'C':1,'T':2,'G':3} 
	d = -2
	result = Needelman_Wunsch_M(seq1,seq2,d,substitution_m,substitution_index)
	Score = result[0]
	Ptr = result[1]
	g.print_matrix(Score)
	g.print_matrix(Ptr)
	start = [len(seq2), len(seq1)]
	end = [0,0]
	al_seqs = Traceback(start,end,seq1,seq2,Ptr)
	g.print_alignment(al_seqs[0],al_seqs[1])
