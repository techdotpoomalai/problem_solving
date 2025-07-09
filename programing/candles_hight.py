candles=[4,4,1,3,4]
maxi=count=0
for height in candles:
    if height>maxi:
        maxi=height
        count=1
        continue
    if height==maxi:
        count+=1
print(count)
