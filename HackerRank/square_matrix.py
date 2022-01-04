#!/bin/python

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
    rows, columns = len(arr), len(arr[0])
    total = rows * columns

    #define incrementor to two diagonals being left to right and right to left
    increment = columns+1
    incrementcolumn = columns-1

    #get itens right to left on diagonal
    rangeRowns = range(0,total,increment)

    #get itens left to right on diagonal
    rangeColumns = range(incrementcolumn,total-incrementcolumn,incrementcolumn)

    count=0;
    SumA=0
    SumB=0
    for item in arr: 
        for x in item:
            if count in rangeRowns:
                SumA=SumA+x
            if count in rangeColumns: 
                SumB=SumB+x

            count=count+1 
    return abs(SumA-SumB)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
