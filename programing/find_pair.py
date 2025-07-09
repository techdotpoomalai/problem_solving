"""this  code working for string """

s="eapple is predpai"
cheked=[]
is_prsend=False
for a in range(len(s)):
    for x in cheked:
        if x==s[a]:     
            is_prsend=True
            break
        else:
            is_prsend=False
    
    if is_prsend or s[a]==" ":
        continue

    count=1
    for b in range(a+1, len(s)-1):
        if s[a]==s[b] and s[a] !=" ":
            count +=1
    
    if count%2 ==0:
        print("{} is pair, that is:{}".format(s[a], int(count/2)))
    else:
        print("{} is not pair".format(s[a]))
    cheked.append(s[a])
print()
        