"""
아직 해결 못함

IndexError: list index out of range --> 구글링 해보면 for 문으로 하면 range error가 발생한다고 나옴
원인 아직 못 찾음
"""
secret = list(input())

for i in range(len(secret)-2): 
    if (secret[i] == "a" or "e" or "i" or "o" or "u" and
        secret[i] == secret[i+2] and secret[i+1] == "p"):
        del secret[i+1:i+2]
    
print(secret)
