# def recrse(n):
#   if n>0:
#     res= n + recrse(n-1)
#     print(res)
#   else:
#     res=0
#   return res

# recrse(6)      


def fun(n):
    return lambda a:a*n

n=int(input())
mydblr=fun(5)
print(mydblr(n))    