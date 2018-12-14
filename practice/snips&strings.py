#Strings and file reading exercises

def palindrome_test(s):
	rev_s=s[-len(s)//2:]
	rev_s=rev_s[::-1]
	if rev_s==s[0:len(s)//2]:
		return True
	else:
		return False
#~ print(palindrome_test('atgcgta'))

def anagram_test(s,t):
	if len(s)==len(t):
		done=[]
		for el in s:
			if el not in done:
				done.append(el)
				s_count=s.count(el)
				t_count=t.count(el)
				if s_count!=t_count:
					return False
		return True
	else:
		return False			
#~ print(anagram_test('atgcgta','aattgggc'))

def DNA_RNA_test(s):
	s=s.upper()
	if 'U' in s:
		return print('RNA')
	else:
		return print('DNA')
#~ print(DNA_RNA_test('augcucga'))

#~ def translation(s):
	#~ start=s.find('atg')
	#~ prot='M'
	#~ stop=s.find('taa')
	#~ codons={'F':['ttt','ttc'],'L':['tta','ttg','ctt','ctc','cta','ctg'],'I':['att','atc','ata'],'M':['gtt','gtc','gta','gtg']}
	
def read_file(path):
	my_file=open(path,'r')
	fasta=my_file.read()
	my_file.close()
	return fasta
#~ prisnt(read_file('prova.fasta'))

def fasta_length(path,path2):
	f=read_file(path)
	length=[]
	g=f.split('\n>')
	for entry in g:
		i=entry.index('\n')
		sqz=entry[i:len(entry)]
		sqz=sqz.replace('\n','')
		with open(path2,'a') as new:
			new.write(str(len(sqz))+'\n')
		length.append(len(sqz))
	return length
#~ print(fasta_length('prova.fasta','res.txt'))




	
	
	
