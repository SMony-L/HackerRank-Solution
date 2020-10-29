#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    print("{} {}".format(sum(arr_sorted[:4]),sum(arr_sorted[1:])))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))