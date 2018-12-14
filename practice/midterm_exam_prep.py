#### exam preparation
# enter the number n
# for every number from 1 to 10
# print the number of rep then a tab and then the product between n and the number of rep
def times_table(n):
	tab=[]
	f=open('res.txt','a')
	for i in range(1,11):
		#~ print('%i\t%i'%(i,i*n))
		tab.append([i,n*i])
		f.write('%i\t%i\n'%(i,i*n))
	f.close()
	return tab

# enter a table 2x2, as a list of lists
# for every list in the list of lists
# print the first item then tab then the second element
def print_table(t):
	for row in t:
		#~ s=''
		#~ for el in row:
			#~ s=s+str(el)+'\t'
		#~ print(s+'\n')
		print('%i\t%i'%(row[0],row[1]))
#~ print_table([[2,4],[5,6]])

# enter a number as a user
# modify times_table
# define empty list tab
# for every from 1 to 10
# make a list of the number of rep and then the product between n and the number of rep
# add the list to tab
# produces a list of lists 
# use list of lists as input for print table

#~ N=int(input('enter a number \n'))
#~ T=times_table(N)
#~ print_table(T)

def filter_homo(path,new_path):
	with open(path,'r') as f:
		fasta=f.read()
	new_file=open(new_path,'a')
	fasta=fasta.split('>')
	for sqz in fasta:
		if 'Homo' in sqz:
			new_file.write(sqz)
	new_file.close()
#~ filter_homo('prova.fasta','res.txt')

def filter_MWW(path,new_path):
	with open(path,'r') as f:
		fasta=f.read()
	new_file=open(new_path,'a')
	fasta=fasta.split('>')
	for sqz in fasta:
		k=0
		for i in sqz:
			if i=='W':		
				k=k+1
		if k>=2:
			lines=sqz.split('\n')
			line_1=lines[1]
			if line_1[0]=='M':
				new_file.write(sqz)
	new_file.close()
#~ filter_MWW('prova.fasta','res.txt')

# a
L=[1,2,3,4,5,6,7,8,9,10]
print(L[4:7])
# b
def first_line(path):
	with open(path,'r') as f:
		line_1=f.readline()
	print(line_1)
#~ first_line('prova.fasta')

var=8
for i in range(var+1):
	print(i**2)

# g.1 'Helloworld' g.2 error cannot implicitly convert integer to string

def odd(n):
	if n%2!=0:
		print(n)
		
#~ odd(5)

L=[]
for i in range(21,40):
	L.append(i)
print(L[-2:])

