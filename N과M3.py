#https://www.acmicpc.net/problem/15650
import sys 
sys.setrecursionlimit(10**6)
history = []

def perm(graph, visit, k, arr):
    if k ==0:
        for i in arr:
            print(i+1, end=' ')
        print()
        return
    
    for i in graph:
        if visit[i] is False:
            arr.append(i)
            perm(graph, visit, k-1, arr)
            arr.pop()


N,M = map(int, sys.stdin.readline().split())
visit = [False for _ in range(N)]
graph = [_ for _ in range(N)]
perm(graph, visit, M, [])
