t = int(input())

for i in range(t):
	
	minSum, maxSum = 0, 0
	n, m = map(int, input().split())
	numList = list(map(int,input().split()))
	
	for j in range(n-m+1):
		comparisonList = numList[j:j+m]
		comparison = 0
		for k in comparisonList:
			comparison = comparison + k
			
		if minSum == 0 or comparison < minSum:
			minSum = comparison
		if comparison > maxSum:
			maxSum = comparison
	
	result = maxSum - minSum
	
	print(f"#{i+1} {result}")
