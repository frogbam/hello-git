#https://www.acmicpc.net/problem/15649
import sys 
sys.setrecursionlimit(10**6)

def perm(graph, visit, k, arr):
    if k ==0:
        for i in arr:
            print(i+1, end=' ')
        print()
        return
    
    for i in graph:
        if visit[i] is False:
            visit[i] = True
            arr.append(i)
            perm(graph, visit, k-1, arr)
            arr.pop()
            visit[i] = False


N,M = map(int, sys.stdin.readline().split())
visit = [False for _ in range(N)]
graph = [_ for _ in range(N)]
perm(graph, visit, M, [])