t = int(input())

for i in range(t):
    input()

    nList = list(map(int, input().split())) # map 함수에 대해서 좀 더 공부
    print(f"#{i+1}",(max(nList) - min(nList))) #f-string 포멧팅 문법 
