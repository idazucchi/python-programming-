# 5 March 2019
# Needelman and Wunsch with no ending gap penalty - but more modularized

import gems as g

def Needelman_Wunsch_M(sq1,sq2,subst_m,subst_i,D):
	# Create the matrices
	S = g.make_matrix(len(sq2)+1,len(sq1)+1)
	P = g.make_matrix(len(sq2)+1,len(sq1)+1)
	# Initialise first row and column
	S[0] = [0 for j in range(len(sq1)+1)]
	for i in range(len(sq2)+1):
		S[i][0] = 0
	# Populate the matrices 
	for i in range(1,len(sq2)+1):
		for j in range(1,len(sq1)+1):
			side = S[i][j-1] + D
			diag = S[i-1][j-1] + subst_m[subst_i[sq2[i-1]]][subst_i[sq1[j-1]]]
			down = S[i-1][j] + D
			res =  g.max_list_position([side,diag,down])
			S[i][j] = res[0]
			P[i][j] = res[1]
	return [S,P]

def max_score_position(S):
	m = len(S[0])-1
	n = len(S)-1
	max_score = S[n][m]
	pos = [n,m]
	for i in range(n+1):
		if S[i][m]>max_score:
			max_score = S[i][m]
			pos = [i,m]		
	for j in range(m+1):
		if S[n][j]>max_score:
			max_score = S[n][j]
			pos = [n,j]	
	return pos

def Traceback(start,stop,sq1,sq2,P):
	# Begin at position start
	I = start[0]
	J = start[1]
	al1 = ''
	al2 = ''
	cell = P[I][J]
	while cell!='*':
		align = {0:[sq1[J-1],'-'],
				 1:[sq1[J-1],sq2[I-1]],
				 2:['-',sq2[I-1]]}
		al1 = al1 + align[cell][0]
		al2 = al2 + align[cell][1]
		move = {0:[-1,0], 1:[-1,-1], 2:[0,-1]}
		J = J + move[cell][0]
		I = I + move[cell][1]
		cell = P[I][J]
	return [al1[::-1],al2[::-1]]


if __name__ == '__main__':
	# Initial input
	seq1 = 'TGATTACA'
	seq2 = 'TGATTA'
	substitution_m = [[2,-1,-1,0],
					  [-1,2,0,-1],
					  [-1,0,2,-1],
					  [0,-1,-1,2]]
	substitution_i = {'A':0,'C':1,'T':2,'G':3}
	d = -2
	results = Needelman_Wunsch_M(seq1,seq2,substitution_m,substitution_i,d)
	Score = results[0]
	Ptr = results[1]
	g.print_matrix(Score)
	g.print_matrix(Ptr)
	start = max_score_position(Score)
	end = '*'
	al_seqs = Traceback(start,end,seq1,seq2,Ptr)
	print('The alignment score is %d'%Score[start[0]][start[1]])
	g.print_alignment(al_seqs[0],al_seqs[1])
