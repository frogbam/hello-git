#https://www.acmicpc.net/problem/2606
import sys

def dfs(g, start_node):
    visited = []
    stack = []
    count = 0
    
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            count += 1
            visited.append(node)
            stack.extend(g[node])

    return count-1
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
g = {i+1:[] for i in range(n)}

for i in range(m):
    frm, to = map(int, sys.stdin.readline().split())
    g[frm].append(to)
    g[to].append(frm)

print(dfs(g, 1))
