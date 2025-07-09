import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    N=len(arr)
    ltor=0
    rtol=0
    for x in range(N):
        for y in range(N):
            if x==y:
                ltor+=arr[x][y]
            if y==N-x-1:
                rtol+=arr[x][y]
    return rtol


arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
if __name__ == '__main__':
    print(diagonalDifference(arr))

    