"find target element index using binary search"
array=[1, 3, 5, 6, 7, 8, 9, 11, 20, 23, 34, 56]
target=1

# array.sort()
start=0
end=len(array)-1

while start <= end:
    mid= (start+end)//2
    if array[mid] == target:
        print("target index is",mid)
        break
    elif array[mid] < target:
        start = mid+1
    else:
        end = mid-1  
print("target not in the list")