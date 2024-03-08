A=int(input("Enter branding expenses:"))
B=int(input("ENter travel expenses:"))
C=int(input("Enter logistics expenses:"))
D=int(input("Enter food expenses:"))
Total=A+B+C+D
e=A*100/Total
f=B*100/Total
g=C*100/Total
h=D*100/Total
print(Total)
print("Branding expenes:{.2f}".format(e))
print("Travel expenes:{}".format(f))    
print("logistics expenes:{}".format(g))
print("Food expenes:{}".format(h))