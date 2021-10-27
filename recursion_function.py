import sys
sys.setrecursionlimit(1000000)
count = 0

def f():
    global count
    count += 1
    print(count)
    f()
f()