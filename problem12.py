import math as m
import time as t

def divisorsofNum(n):
    nod = 0
    sqrt = (int)(m.sqrt(n))
    for i in range(1,sqrt):
        if n%i==0:
            nod += 1
    nod = nod * 2
    return nod

def main():
    triangleNum = 0
    i = 1
    while divisorsofNum(triangleNum) < 500:
        triangleNum += i
        i += 1
    print(triangleNum)

starttime = t.time()
main()
print(t.time()-starttime)