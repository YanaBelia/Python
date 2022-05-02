'''Heming network model for simple pattern recognition.'''

class func:

    def __init__(self):
        self.n3 = [1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1]
        self.l=len(self.n3)
        self.T=len(self.n3)/2

    def Print(self, list):

        ney1=[];L=[];
        for i in list:
            if i==1:ney1.append('[#]')
            else:ney1.append('[ ]')
        for i in range(1,len(ney1)):
            while len(ney1)!=0:
                a=ney1[:4]
                L.append(a)
                ney1=ney1[4:]
        for elem in L:print(''.join(elem),'\t')

    def weight(self, n, w):
        for elem in n:
            w.append(elem/2)
        return w

    def U1(self, func1 ):
        i=0
        B=[]
        while i<self.l:
            B.append(func1[i]*self.n3[i])
            i+=1
        N=self.T+sum(B)
        return N

    def result(self, u1, u2):
        if u1>u2:
            #print('Зашумлений образ ближчий до образу 1')
            print('The noisy image is closer to the image 1')
        #elif u1<u2:print('Зашумлений образ ближчий до образу 2')
        elif u1<u2:print('The noisy image is closer to the image 2')
        #else:print('Подібність образу визначити неможливо')
        else:print('It is impossible to determine the similarity of the image')



if __name__ == "__main__":
    weight2=[]
    weight1=[]
    n1=[-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1]
    n2=[1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,-1,-1,1]
    n3=[1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1]
    func = func()

    print('The matrix of the reference image 1: ')
    func.Print(n1)
    #print('Матриця еталонного образу 2: ')
    print('The matrix of the reference image 2:')
    func.Print(n2)
    print('Noisy image : ')#зашумлений образ
    func.Print(n3)

    W1 = func.weight(n1, weight1);W2 = func.weight(n2, weight2)
    print('Weight matrix 1 -->', W1)
    print('Weight matrix 2 -->', W2)

    u1 = func.U1(W1); u2 = func.U1(W2)
    print(f'U(1,1) --> {u1}')
    print(f'U(1,2) --> {u2}')

    func.result(u1, u2)
