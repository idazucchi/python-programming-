# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code:
open the file sprot_prot.fasta
read all lines from file
concatenate all lines together in one string S 
close the fasta file
split S on > to obtain a list of entries
prepare list string no_homo
for every entry perform the following actions:
	if Homo sapiens isn't contained in the entry:
		add the entry to no_homo list
		isolate header
		to isolate the species find the 'OS' in the header
		find the 'GN' in the header that is the elment that follows the species
		the species is the part of the header between 'OS' and 'GN'
		isolate sequence
		sequence=sequence stripped of '\n'
		print length of sequence
 open new file
 print no_homo to the new file
'''

def read_fasta(path):
	with open(path,'r') as f:
		content=f.readlines()
		S=''
		for line in content:
			S=S+line		
	return S
#~ print(read_fasta('sprot_prot.fasta'))

def no_homo(path):
	S=read_fasta(path)
	no_homo=[]
	S=S.split('>')
	for entry in S:
		if 'Homo sapiens' not in entry and entry!='':
			no_homo.append(entry)
	return no_homo		#output is a list of entries
		
def save_to_file(l,path):     #input is a list of entries
	s=''
	for entry in l:           #transforms the list of entries to one string
		s=s+entry
	with open(path,'a') as new_f:
		new_f.write(s)               #saves the etries string to a file

def sequence_length(l):
	for entry in l:
		i=(entry.index('\n'))
		header=entry[0:i]     #isolates the header from the entry
		os_i=header.index('OS=')+3   #+3 allows to exclude 'OS=' from the slice at line 63
		gn_i=header.index('GN')
		os=header[os_i:gn_i]
		sequence=entry[i:]      #isolates the sequence from the entry
		sequence=sequence.replace('\n','')  #delete extra characters to evaluate correctly the sequence length
		length=len(sequence)
		print('the sequnce comes from %s and is %.0f long'%(os,length))		


no_homo_entries=no_homo('sprot_prot.fasta')  #LIST
save_to_file(no_homo_entries,'no_homo.txt')  #output to file
sequence_length(no_homo_entries)	         #output to screen
