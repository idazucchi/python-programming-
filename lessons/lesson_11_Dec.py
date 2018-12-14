#lesson 11 December 2018

def vector_mean(v):
	a=0
	for el in v:
		a=a+el
	return a/len(v)
	
def variance(v):
	summ=0
	mean=vector_mean(v)
	for el in v:
		summ=summ+pow(el-mean,2)
	variance=summ/(len(v)-1)   #Bessel's correction
	return variance

def standard_deviation(v):
	return pow(variance(v),1/2)

#Read file and split values in two lists: L1 are primary nurons dedrite lengths, L2 are secondary neurons dendrite lengths	
L1=[]
L2=[]
with open('neuron_data2.txt','r') as f:
	for line in f:
		line=line.split()
		if line[0]=='1':
			L1.append(float(line[1]))
		elif line[0]=='2':
			L2.append(float(line[1]))
print(L1,L2)
#compute mean and standar dev for each group L1, L2
mean_L1=vector_mean(L1)
mena_L2=vector_mean(L2)
print(mena_L2,round(mean_L1,4),mena_L2<mean_L1)
st_dev_L1=standard_deviation(L1)
st_dev_L2=standard_deviation(L2)
print(st_dev_L1,st_dev_L2)
#compute MAX and min value for each group
print('The minimum length for L1 is %f and the maximum is %f'%(min(L1), max(L1)))
print('The minimum length for L2 is %f and the maximum is %f'%(min(L2), max(L2)))
#compute number of entries for each group
print('The number of entries for L1 is %d while for L2 is %d'%(len(L1),len(L2)))

#reconstrut the data table into a new file
with open('neuron_tab.txt','w') as new_f:
	for el in L1:
		new_f.write('1\t%f\n'%el)   #for each length in L1 
		#~ new_f.write('1\t'+str(el)+'\n')  #equivalent to the line above
	for el in L2:
		new_f.write('2\t%f\n'%el)   #for each length in L1 
		#~ new_f.write('2\t'+str(el)+'\n')  #equivalent to the line above
	
	

