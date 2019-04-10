# 6 March 2019
# Viterbi algorithm but more modularised
import gems as g

def max_list_position(l):
	max_val = l[0]
	pos = 0
	for e in range(len(l)):
		if l[e]>max_val:
			max_val = l[e]
			pos = e
	return [max_val,pos]

def best_transition(i,j,states,trans_p,V):
	# Determine best transition to state i
	l = []
	for k in range(len(states)):
		contribute = V[k][j-1] * trans_p[k][i]
		l.append(contribute)
	best = max_list_position(l)
	return best

def Viterbi_M(sq,states,trans_p,emiss_p,h_emission_i):
	sq = '-' + sq + '-'
	# Create probability and pointer matrices
	V = [['*' for j in range(len(sq))] for i in range(len(states))] 
	P = [['*' for j in range(len(sq))] for i in range(len(states))] 
	# Initialise first row
	V[0][0] = 1
	for i in range(1,len(states)):
		V[i][0] = 0
	# Compile the matrix col by col, left to right
	for j in range(1,len(sq)-1):
		sq_char = sq[j]
		for i in range(len(states)):
			# Store probability and pointer
			best_trans = best_transition(i,j,states,trans_p,V)
			V[i][j] = best_trans[0] * emiss_p[i][h_emission_i[sq_char]]
			P[i][j] = best_trans[1]
	# End of matrices
	last_trans = best_transition(len(states)-1,len(sq)-1,states,trans_p,V)
	V[len(states)-1][len(sq)-1] = last_trans[0]
	P[len(states)-1][len(sq)-1] = last_trans[1]	
	return [V,P]
			
def Traceback(sq,states,P):
	I = len(states)-1
	J = len(sq)+1
	path = 'e'
	while (I!=0) and (J!=0):
		cell = P[I][J]
		path = path + states[cell]
		J = J -1
		I = cell	
	return path[::-1]

if __name__ == '__main__':
	# Initial input
	seq = 'ATCGCGTGGT'
	States = ['b','Y','N','e']
	transition_p = [[0,0.2,0.8,0],
					[0,0.7,0.2,0.1],
					[0,0.1,0.8,0.1],
					[0,0,0,0]]
	emission_p = [[0,0,0,0],
				  [0.1,0.4,0.4,0.1],
				  [0.25,0.25,0.25,0.25],
				  [0,0,0,0]]
	H_emission_i = {'A':0,'C':1,'G':2,'T':3}
	# Compute the Viterbi and pointer matrices
	results = Viterbi_M(seq,States,transition_p,emission_p,H_emission_i)
	V = results[0]
	Ptr = results[1]
	g.print_matrix(V)
	g.print_matrix(Ptr)
	Viterbi_path = Traceback(seq,States,Ptr)
	print("the Viterbi path for the sequence %s\n is %s\n with a probability of %r"%(seq,Viterbi_path,'{:.2e}'.format(V[len(States)-1][len(seq)+1])))
