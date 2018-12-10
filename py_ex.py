#Ex 001
import math, random

def ex_001(first_var):
	y=3.14
	print(first_var)
	if x%2==0:
		print('%s is even'%first_var)
	else:
		print('%s is odd'%first_var)
	a=(first_var+y)/2
	print('the average of x and y is ',a)
	d_x=abs(a-first_var)
	d_y=abs(a-y)
	print(d_x,d_y)
	d_a=(d_x+d_y)/2
	print(d_a)

x=7
y=3.14
#print(x)
if x%2==0:
	print('even')
else:
	print('odd')
##EEEEEHHHHH????
#~ if type(x//2)==float:
	#~ print('odd',type(x//2))
#~ else:
	#~ print('even',type(x//2))
a=(x+y)/2
#print(a)
d_x=abs(a-x)
d_y=abs(a-y)
#print(d_x,d_y)
d_a=(d_x+d_y)/2
#print(d_a)
z=(x*2)-1
#ex_001(z)
t=5
def euclidean_d(x1,y1,x2,y2):
	euc_d=math.sqrt((math.pow((x1-x2),2))+(math.pow((y1-y2),2)))
	return euc_d
#print(euclidean_d(4,0,0,3))
#print(euclidean_d(x,z,y,t))
probability= random.uniform(0.0, 1.0)
info_content=math.log(probability,2.0)
#print(probability, info_content)

#Ex 002

def ex_002(s):
	print(s[2], s[4], s[9], s[-1], s[-2], len(s) )
	even=''
	odd=''
	for position in range(0,len(s)):
		if position%2==0:
			even=even+str(s[position])
		else:
			odd=odd+str(s[position])
	print('even characters of the string: %s \nodd characters of the string: %s ' %(even,odd))
	l=(len(s)//2)+1
	print('first half of the string: %s'%s[0:l])
	rev=''
	for i in range(1,len(s)):
		rev=rev+s[-i]
	rev=rev+s[0]
	print('the string in reverse order: %s'%rev)
	print('the number of I is %d, the number of E is %d' %(s.count('i'), s.count('e')))
	ees=[]
	for i in range(0,len(s)):
		if s[i]=='e':
			ees.append(i)
	print('the first E is at position %s and the last one is at position %s'%(ees[0], ees[-1]))
	
s='fire and ice'
#~ ex_002(s)
#~ ex_002('Magical mystery tour is waiting to take you away')
ex_002('Kind of blue')
#~ a=s.replace('and','&')
#~ print(a)
#~ print('fire' in s, 're and' in s, 're &' in s)
#~ print(s.find('e'), s.index('e'))
#~ pi='234432976548923'
#~ add='3'
#~ add_n=float(add*len(pi))
#~ print(add_n,add_n+float(pi) )
