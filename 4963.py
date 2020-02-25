#섬의 개수
#https://www.acmicpc.net/problem/4963
import sys


def findIsland(graph, w, h):
    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count+=1
                graph[i][j] = 0
                lookAround(graph, i, j, w, h)
    print(count)
                
def lookAround(graph, i, j, w, h):
    di = [-1,-1,-1,0,0,1,1,1]
    dj = [-1,0,1,-1,1,-1,0,1]
    queue = [[i,j]]

    while queue:
        v = queue.pop(0)
        for k in range(8):
            i = v[0]+di[k]
            j = v[1]+dj[k]
            if 0<= i <=h-1 and 0 <= j <=w-1 and graph[i][j]: 
                graph[i][j] = 0
                queue.append([i,j])
            

while(1):
    graph = []
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    findIsland(graph, w, h)
