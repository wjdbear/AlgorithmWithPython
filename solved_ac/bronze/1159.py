numLineup = int(input())

lineup = []

for i in range(numLineup):
	firstname = input()
	lineup.append(firstname[0])

tmplineup = sorted(list(set(lineup)))
surrend = 0

for k in tmplineup:
	if lineup.count(k) >= 5:
		print(k,end='')
	else:
		surrend += 1
		
if surrend == len(tmplineup):
	print("PREDAJA")
