words = input().upper()
org_words = list(set(words))

count_list = [] 

for i in org_words:
    count = words.count(i)
    count_list.append(count) # [4,1,1,4]

if count_list.count(max(count_list)) > 1:
    print("?")
    
else:
    loc = count_list.index(max(count_list))
    print(org_words[loc])
