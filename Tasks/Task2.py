'''Пошук в кожному рядку елемент з найменшим значенням, а потім серед цих чисел вибір найбільшого.
Search in each row the element with the smallest value, and then among these numbers choose the largest.'''
import numpy as np
import random


def result(m, n, matrix):
    L=[]
    for i in range(n):
        mn = 100
        for j in range(m):
            if matrix[i][j] < mn:
                mn = matrix[i][j]
        for i in range(n):
            for j in range(m):
                if mn == matrix[i][j]:
                    print('Row: %d, col: %d' % (i+1,j+1),',element:',mn)
        L.append(mn)

    print('The maximum of the minimum elements is:',max(L))

if __name__ == "__main__":
    n, m=5, 5  
    x=[0]*m
    y=[0]*n
    for i in range(m):
    	x[i]=[0]*n
    	for j in range(n):
    		y[j]=[0]*m
    		x[i][j] = random.randint(-100,100)
    matrix=np.array(x)
    print(matrix,end='\n')
    result(m, n, matrix)
