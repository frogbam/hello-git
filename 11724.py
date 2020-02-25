#연결요소의 개수
#https://www.acmicpc.net/problem/11724
#https://rebas.kr/653
import sys
sys.setrecursionlimit(10000)

def DFS(graph):
    V = len(graph)+1
    visited = [False]*(V)
    count = 0

    for i in range(1, V):
        if not visited[i]:
            count += 1
            DFSUtil(graph, i, visited)
    
    return count

def DFSUtil(grapoh, v, visited): 


    visited[v]= True
    for i in graph[v]: 
        if visited[i] == False: 
            DFSUtil(graph, i, visited) 


N,M = map(int, sys.stdin.readline().split())


graph = {}
for n in range(N):
    graph[n+1] = []
    
for m in range(M):
    key,value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

print(DFS(graph))