'''given an array of integer and a target sum, return indices of the two numbers that add up to the target '''

array =[1,2,3,4,5,6,7,8,9,10]
target =4

for x in range(len(array)-1):
    for y in range(x+1,len(array)):
        if array[x]+array[y]==target:
            print(x,y)