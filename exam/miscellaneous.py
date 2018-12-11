# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
L=[]
for i in range(21,40):
	L.append(i)
even=[]
for element in L:
	if element%2==0:
		even.append(element)
triple=[]
for element in L:
	if element%3==0:
		triple.append(element)
print('the even numbers in the list L are ',even,'\nthe numbers multiple of 3 in th elist L are ',triple)

# Exercise 2
# Print the last two elements of L 
print(L[-2:])

# Exercise 3
# What's wrong with the following piece of code? Fix it and --> missing :, wrong indentation, mixed use of tab and spaces to indent
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once
T = ['1', '2', '3']
for i in range(10):
	if str(i) in T:
		print('%d is in the list'%i)
	else:
		print('%d not found'%i)    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 
with open('sprot_prot.fasta','r') as fastaf:
	line_1=fastaf.readline()
	line_1=line_1.split('OS=')
	line_1_1=line_1[1]
	print(line_1_1)

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
line_1_1=line_1_1.split(' ')
conc=line_1_1[0]+line_1_1[1]
print(conc)

# Exercise 6
# reverse the string 'asor rosa'
s='asor rosa'
rev_s=s[::-1]
print(rev_s, s==rev_s)  # s==rev_s returns True if s is a palindrome, False if s is no palindrome

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
L = [1, 7, 3, 9]
L.sort()
print(L)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
L = [1, 7, 3, 9]
sorted_L=L.sort()
print(sorted_L)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
tab=[[2,4],[3,6]]
with open('tab.txt','a') as outp_f:
	for row in tab:
		outp_f.write('%i\t%i\n'%(row[0],row[1]))
