from math import sqrt
def tub(x):
    m = True
    if x == 1:
        m = False
    elif x>1:
        for j in range(2,int(sqrt(x))+1):
            if x%j == 0:
                m = False
    return m

n = int(input())
c = 0
for i in range(1,(n)//2+1):
    if tub(i) == 1:
        if tub(n - i) == 1:
            c = 1
            print(i,'+',n - i,'=',n)
            break
if c == 0:
    print('-1')