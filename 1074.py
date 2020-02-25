#Z
#https://www.acmicpc.net/problem/1074
#https://pacific-ocean.tistory.com/225

import sys

count = 0

def z(N,r,c, root):
    global count
    print("*"*10, N)
    print(root)
    if N==1:
        i = root[0]
        j = root[1]
        if i == r and j == c:
            print(0+count)

        elif i == r and j+1 == c:
            print(1+count)

        elif i+1 == r and j == c:
            print(2+count)

        elif i+1 == r and j+1 == c:
            print(3+count)
        count = count+4
        return
        
    i = root[0]
    j = root[1]
    r= r-i
    c = c-j
    n = (2**N)
    m = (2**(N-1))
    #어느 사분면에 있는지 탐색
    #0사분면
    if  0<= r <=m-1 and 0<= c <=m-1:
        count += 2**(2*(N-1))*0
        i = root[0]
        j = root[1]
        print("0사분면")
    #1사분면
    if 0<= r <= m and m<= c <=n-1:
        count += 2**(2*(N-1))*1
        
        i = root[0]
        j = root[1]+2**(N-1)
        print("1사분면")
    #2사
    if m <= r <= n-1 and 0<= c<= m:
        count += 2**(2*(N-1))*2
        i = root[0]+2**(N-1)
        j = root[1]
        print("2사분면")
    #3
    if m<= r<=n-1 and m<=c<=n-1:
        count += 2**(2*(N-1))*3
        i = root[0]+2**(N-1)
        j = root[1]+2**(N-1)
        print("3사분면")
    print(i,j)
    z(N-1, r, c, (i,j))
    
N, r, c = map(int, sys.stdin.readline().split())
first = (0,0)
z(N, r, c, (0,0))

