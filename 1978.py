# 소수 찾기
# https://www.acmicpc.net/problem/1978
import sys
import math

def isPrime(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))
count = 0
for num in nums:
    if isPrime(num):
        count = count+1
print(count)