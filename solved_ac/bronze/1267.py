numCall = int(input())

callTime = list(map(int,input().split()))

Ybill = []
Mbill = []

for i in callTime:
	Ybill.append((i//30+1)*10)
	Mbill.append((i//60+1)*15)
	
if sum(Ybill) > sum(Mbill):
	print("M "+str(sum(Mbill)))

elif sum(Ybill) < sum(Mbill):
	print("Y "+str(sum(Ybill)))
	
else:
	print("Y M "+str(sum(Ybill)))
