#테트로미노
#https://www.acmicpc.net/problem/14500

import sys

def brute():
    pass


n, m = map(int, sys.stdin.readline().split())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

brute(paper)
