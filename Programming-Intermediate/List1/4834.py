#아직 다 못함 -> 보완 에정
t = int(input())

for i in range(t):
	n = int(input())
	numCard = input()
	cardList = []
	for j in numCard:
		cardList.append(j)
	orgCardList = list(set(cardList))
	
	maxNum = 0
	
	for k in range(len(orgCardList)):
		result = cardList.count(orgCardList[k])
		if maxNum < result:
			maxNum = result
			number = orgCardList[k]
		if maxNum == result:
			if number
			
	print("#%s %s %s" %(i+1,number,maxNum))
