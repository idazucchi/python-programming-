#scalar by points

def scalar_by_point(s,v):
	v1,v2= v
	return [(v1*s),(v2*s)]
#~ print(scalar_by_point(4,(4,2)))

def Bernstein(i,n,t):
	from math import factorial as fact
	

#~ Bernstein()

#~ with open('gff_prova.gff','r') as f:
	#~ for line in f:
		#~ if 'Mutagenesis' in line:
			#~ #if '043' in line:
			#~ position=line.index('->')
			#~ print(line[position-1:position+10])

def scalar_prod(s,v):
	vs=[]
	for element in v:
		vs.append(s*element)
	return vs
V=[1,2,3,'ciccia']   
#~ print(scalar_prod(2,V))

def base_counting(sequence,base):
	base_n=0
	sequence=sequence.upper()
	for elem in sequence:
		if base==elem:
			base_n=base_n+1
	return base_n
#~ print(base_counting('actgttat','t'))

def base_frequency(sequence):
	l=len(sequence)
	print(l)
	a=base_counting(sequence,'A')/l
	t=base_counting(sequence,'T')/l
	c=base_counting(sequence,'C')/l
	g=base_counting(sequence,'G')/l
	return [a,t,c,g]
#~ print(base_frequency('aacct'))

def vector_mode(v):
	done=[]
	max_rep=0
	mode= float
	for element in v:
		if element not in done:
			done.append(element)
			a=v.count(element)	
			if a>max_rep:
				mode=element
				max_rep=a
	return mode
#~ print(vector_mode([1,3,5,1,8,2,6,3,3,2,4,4,4,4,4,4,4]))

def vector_mean(v):
	a=0
	for el in v:
		a=a+el
	return a/len(v)
#~ print(vector_mean([10,8,9]))
		
def fact(n):
	fact=1
	for i in range(1,n+1):
		fact=i*fact
		print( i)
	return fact
#~ print(fact(5))	

def vector_median(v):
	l=len(v)
	h=l//2
	if l%2==0:
		median=(v[h-1]+v[h])/2
	else:
		median=v[h]
	return median
#~ print(vector_median([10,8,9,5,4]))	

def variance(v):
	summ=0
	mean=vector_mean(v)
	for el in v:
		summ=summ+pow(el-mean,2)
	variance=summ/(len(v)-1)     #Bessel's correction
	return variance
#~ print(variance([10,8,9,5,4]))

def standard_deviation(v):
	return pow(variance(v),1/2)
#~ print(standard_deviation([10,8,9,5,4]))

def z_value(v):
	mean=vector_mean(v)
	st_dev=standard_deviation(v)
	z_val=[]
	for el in v:
		z=(el-mean)/st_dev
		z_val.append(z)
	return z_val
#~ print(z_value([10,8,9,5,4]))

def vector_sum(a,b):
	c=[]
	if len(a)==len(b):
		for i in range(len(a)):
			c.append(a[i]+b[i])
		return c
	else:
		return print('Vectors of different dimension cannot be summeds')
#~ print(vector_sum([4,3,2],[4,5,3]))

def vector_scalar_prod(a,b):
	c=0
	if len(a)==len(b):
		for i in range(len(a)):
			c=c+((a[i])*(b[i]))
		return c
	else:
		return print('Vectors of different dimension cannot be multiplied')
#~ print(vector_scalar_prod([4,3,2],[4,5,3]))

def vector_distance_square(a,b):
	c=0
	if len(a)==len(b):
		for i in range(len(a)):
			c=c+pow((a[i]-b[i]),2)
		return c
	else:
		return print('The two vectors do not belong to the same space')
#~ print(vector_distance([3,4],[0,4]))

def vector_distance(a,b):
	return pow(vector_distance_square(a,b),1/2)

def RMSD(a,b):
	if len(a)==len(b):
		c=0
		k=0
		for el in a:
			c=c+vector_distance_square(a[k],b[k])
			k=k+1
		RMSD=pow(c/len(a),1/2)
		return RMSD
	else:
		return print('Cannot compute RMSD, uneven length of sequences')
#~ print(RMSD([[3,4],[0,4]],[[3,4],[0,4.17]]))
	
def matrix_row_sum(M):
	S=[]
	for row in M:
		row_sum=0
		for number in row:
			row_sum=row_sum+number
		S.append(row_sum)	
	return S
#~ print(matrix_row_sum([[2,3,1],[5,4,2],[3,5,6]]))
	
def matrix_sum(A,B):
	if len(A)==len(B):
		C=[]
		for row_n in range(len(A)):
			if len(A[row_n])==len(B[row_n]):
				print(row_n,'row')
				temp_row=[]
				A_row=A[row_n]
				B_row=B[row_n]
				#~ print(A_row,B_row)
				for number in range(len(A_row)):
					print(number)
					temp_row.append(A_row[number]+B_row[number])
				C.append(temp_row)
			else:
				return print('The number of columns is uneven')
		return C		
	else:
		return print('These matrices have different dimensions and cannot be summed')
#~ print(matrix_sum([[2,3,1],[5,4,2],[3,5,6]],[[2,3,0],[5,4,0],[3,5,0]]))




	
