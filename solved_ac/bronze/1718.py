plainText = list(input())
enKey = list(input())

cryptogram = []

share, reaminder = divmod(len(plainText),len(enKey))

keyList = (enKey * share) + enKey[:reaminder]

for i in range(len(plainText)):
	charAscii = ord(plainText[i])-ord(keyList[i])
	if (plainText[i] == " "):
		cryptogram.append(plainText[i])
	elif (charAscii > 0):
		cryptogram.append(chr(96+charAscii))
	else:
		cryptogram.append(chr(122-(int(ord(keyList[i])-ord(plainText[i])))))
		
for j in cryptogram:
	print(j,end="")
