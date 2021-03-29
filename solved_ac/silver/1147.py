candidate = int(input())
canList = []

for i in range(candidate):
    canList.append(int(input()))

dasom = canList[0]
otherCand = canList[1:-1]

if candidate == 1:
    print(0)
else:
    result = 0
    otherCand = sorted(otherCand, reverse=True)
    while otherCand[0] >= dasom:
        dasom += 1
        otherCand[0] -= 1
        result += 1
        otherCand = sorted(otherCand, reverse=True)
    print(result)
