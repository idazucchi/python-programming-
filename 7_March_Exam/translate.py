# March 7th, 2019 - Ida Zucchi - Midterm

import sequence_data as sd

# Given a DNA sequence returns the corresponding RNA sequence
def dna2rna(sq):
	sq = sq.upper()
	rna = sq.replace('T','U')
	return rna

# Given a sequence of DNA it returns the corresponding aminoacid sequence
def translate(seq):
	try:
		seq = seq.upper()
		if all(c in sd.dna_symbols for c in seq): 
			rna = dna2rna(seq)
		prot = ''
		for e in range(0,len(rna),3):
			prot += sd.genetic_code[rna[e:e+3]]
		return prot
	except:
		print('the input sequence id not DNA')
		return ''
	
	
if __name__ == '__main__':
	# Initial input
	dna = sd.dna_seq
	print(translate(dna))
	print(translate('AUGGAGUGGUAG'))

