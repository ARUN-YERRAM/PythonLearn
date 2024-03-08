from time import time

def fun1(a,b):
    #ram
    return a+b

def fun2(a,b):
    #rohan
    if(a>b) or a!=b:
        pass
        sum([3,4])
        return a+b

if __name__== '__main__':
    init=time()
    for i in range(0,100000):
        fun1(3,5)
    # print("Ram das time",time()-init)
    # init=time()
    for i in range(0,1000):
        fun2(7,8)
    print("overall execution time",time()-init)


