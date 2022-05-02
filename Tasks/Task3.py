'''Множення матриць 4*4 методом Винограда.
Multiplication of 4 * 4 matrices by the Grape method.'''
import numpy as np

def print_matrix(matrix, name):
    print(f'\nMatrix {name}:\n{np.array(matrix)}')


def step1(list, len_):
    d=[]
    row_or_column_factor=[]
    for elem in list:
        for x in range(len_):
            if x%2==0:i=x
            else:
                j=x
                s=elem[i]*elem[j]
                d.append(s)
    for i in range(1,len(d)):
        while len(d)!=0:
            a=d[:2]
            row_or_column_factor.append(sum(a))
            d=d[2:]
    return row_or_column_factor

def result(A, B, B1, n, step1_result, step1_result1):
    C=[];C1=[]
    for i in range(n):
        for j in range(n):
            c=(A[i][0]+B[1][j])*(A[i][1]+B[0][j])+(A[i][2]+B[3][j])*(A[i][3]+B[2][j])-step1_result[i]-step1_result1[j]#формула
            C.append(c)
    for i in range(1,len(C)):
        while len(C)!=0:a=C[:4];C1.append(a);C=C[4:];
    return np.array(C1)


if __name__ == "__main__":
    A=[[1,6,8,56],
        [3,9,0,7],
        [4,2,69,8],
        [6,7,2,1]]
    B=[[11,9,6,5],
        [34,2,10,1],
        [76,3,0,7],
        [61,0,2,1]]
    B1=[]
    for elem in list(zip(*B)):
        B1.append(list(elem))

    step1_result = step1(A, len(A))
    step1_result1 = step1(B1, len(B1))

    print_matrix(A, 'A')
    print_matrix(B, 'B')
    print(f'\nRowfactor--> {step1_result}')
    print(f'\nColumnfactor--> {step1_result1}')
    print(f'\nMatrix C=(A*B)\t \n{result(A, B, B1, len(A), step1_result, step1_result1)}')
