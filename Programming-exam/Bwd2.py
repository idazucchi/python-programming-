# 6 March 2019
# Backward algorith but more modularised

def Backward(sq,states,trans_p,emiss_p,h_emission_i):
	B = [['*' for j in range(len(sq)+1)] for i in range(len(states))]
	# Initialise last column
	for i in range(len(states)):
		B[i][len(sq)] = trans_p[i][len(states)-1]
	# Compile the matrix
	for j in range(len(sq)-1,-1,-1):
		for i in range(len(states)):
			l = []
			for k in range(len(states)):
				contribute = B[k][j+1] * trans_p[i][k] * emiss_p[k][h_emission_i[sq[j]]]
				l.append(contribute)
			B[i][j] = sum(l)
	return B



if __name__ == '__main__':
	# Initial input
	seq = 'ATCGC'
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
	# Compute the p(s|HMM)
	M = Backward(seq,States,transition_p,emission_p,H_emission_i)
	print("The p(s|M) for the sequence %s\n is %r"%(seq,M[0][0]))
