#골드바흐의 추측
#https://www.acmicpc.net/problem/6588

import sys
import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

def checkConjecture(target):
    #4
    half = int(target/2)
    
    for i in range(half+1):
        if not isPrime(i):
            continue
        
        if isPrime(target - i):
            return "%d = %d + %d\n" %(target, i, target-i)
    
    return "Goldbach's conjecture is wrong."

targets = []
while(1):
    target = int(sys.stdin.readline())
    if target == 0:
        break
    targets.append(target)

for target in targets:
    sys.stdout.write(checkConjecture(target))
