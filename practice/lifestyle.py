print('Is this lifestyle sustainable? AKA Am I going to burn out?\n Find out with this handy program!')
print("Let's start by understanding how you spend your time\n for the next requests type in the time you spend daily performing the indicated activity on average")
sleep=float(input('Sleeping\n'))
eat=float(input('Eating\n'))
toilet=float(input('Bathroom time\n'))
commute=float(input('Commuting\n'))
Thing=float(input('Time Consuming Thing\n'))
nFT=float(input('Now estimate how much free time you need in a day to function well \n'))
AFT=(24 -sleep -toilet -eat -commute -Thing)
#~ w_AFT=(24 -sleep -toilet -eat -commute -Thing)
#~ AFT=w_AFT*5 +(w_AFT+Thing)*2
#~ Theoretical_study=36*2 #stima conservativa per una settimana di lavoro: n di ore di lezione * 2 (ammettendo che i CFU siano ripartiti come 1/3 lezione + 2/3 studio autonomo)
if AFT< nFT:
	print('You are fried! \n You need to rearrange something')
else:
	print('You are getting by c:')
print(AFT- nFT)
#~ if AFT< Theoretical_study:
	#~ print('You are fried! \n You need to rearrange something')
#~ else:
	#~ print('You are getting by c:')
#~ print(AFT- Theoretical_study)
