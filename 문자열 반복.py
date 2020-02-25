import sys
t = int(sys.stdin.readline())
for i in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)
    for i in s:
        print(i*r, end='')
    print()
