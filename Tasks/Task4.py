'''Half-division method'''
import math

def f(x):
    return math.exp(x)-x**2-3

def func(a, b, eps):
    A=[];B=[];C=[];vec=[];
    while abs(f(b)-f(a)) > eps:
        c = (a+b) / 2
        if f(c) == 0 or abs(f(c)) < eps:
            print(f'The root is at the point x = {c}\n')
            print(f'f(x)={f(c)}\n')
            for i in range(len(A)):
                print ("xl: %-*s xx: %-*s xr: %-*s" % (22, A[i],22, C[i],22,  B[i]))
            print(f'iter --> {str(len(A))}')
            break
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        A.append(a)
        B.append(b)
        C.append(c)
    else:
        print('The root is not found')
func(-10, 10, 0.0001)
