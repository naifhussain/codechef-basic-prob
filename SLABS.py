T = int(input())
for t in range(T):
	S = int(input())
	if(S>1500000):
		S -= (250000*0.75)+(S-1500000)*0.3
	elif(S>1250000):
		S -= (250000*0.5)+(S-1250000)*0.25
	elif(S>1000000):
		S -= (250000*0.3)+(S-1000000)*0.2
	elif(S>750000):
		S -= (250000*0.15)+(S-750000)*0.15
	elif(S>500000):
		S -= (250000*0.05)+(S-500000)*0.1
	elif(S>250000):
		S -= (S-250000)*0.05
	print(int(S))