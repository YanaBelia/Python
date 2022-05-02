from functools import reduce

def func():
    L=[22,65,90,34,5,8,91,12,89,6]
    a = L[0]
    for i in range(1, len(L)):
        if L[i] > a:
            a = L[i]
    b=L.index(a)
    L1=L[:b]
    L2=L[b+1:]
    print(L)
    print('max value=',a)
    print(f'values before {a}-->{L1}')
    print('sum = ',sum(L1))
    print(f'values after {a}-->{L2}')
    print('ploduct of these values =',reduce(lambda x, y: x*y, L2))
func()
