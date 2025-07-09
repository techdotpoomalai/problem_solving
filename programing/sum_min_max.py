arr=[11,6,3,5,7,9]
mini=maxi=-1
start=True
for x in range(len(arr)):
    sum=0
    for y in range(len(arr)):
        if x==y:
            continue
        else:
            sum+=arr[y]
    if sum>maxi:
        maxi=sum
        if start:
            mini=maxi
            start=False
    elif mini>sum:
        mini=sum
        
print(mini,maxi)