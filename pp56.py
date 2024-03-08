n=int(input("enter n:"))
flag=0
for i in range(0,n):
    for j in range(0,n):
        if(i**2+j**2==n):
            flag=1
            break

if flag==1:
    print("True")
else:
    print("False")            