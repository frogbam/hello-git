#일곱 난쟁이
#https://www.acmicpc.net/problem/2309
from itertools import combinations
import sys

dwarfs = []
for i in range(9):
    dwarfs.append(int(sys.stdin.readline()))

dwarfs.sort()

cases = list(combinations(dwarfs,7))
sum = 0

for case in cases:
    sum = 0
    for height in case:
        sum += height
    
    if sum == 100:
        for real in case:
            print(real)
        break






