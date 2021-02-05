#아직 방법 찾는 
count = int(input())

for i in range(count):
	k,n,m = map(int, input().split())
	busRoute = list(map(int, input().split()))
	
	for j in range(len(busRoute)-1):
		if busRoute[j+1] - busRoute[j] > k and busRoute[0] > k:
			print(f"#{i+1} 0")
		else:
			for k in 
			#minCharge = n // k
