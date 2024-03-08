star=lambda x,y:x+y
def small(a,b):
    print(star(a,b))
    if a<b:
        print (a)
    else:
        print(b)
    
k,z=[int(i) for i in input('enter value:').split()]
small(k,z)
