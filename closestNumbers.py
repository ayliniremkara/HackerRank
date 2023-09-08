#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    pairs = []
    min_difference = abs(arr[0] - arr[len(arr) - 1])

    for i in range(1, len(arr)):
        difference = abs(arr[i] - arr[i - 1])

        if difference < min_difference:
            min_difference = difference
            pairs = [(arr[i - 1], arr[i])]
        elif difference == min_difference:
            pairs.append((arr[i - 1], arr[i]))

        flat_list = []
        for sublist in pairs:
            for item in sublist:
                flat_list.append(item)
    return flat_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
