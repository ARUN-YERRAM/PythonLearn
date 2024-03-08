
# It was Christmas Eve and the celebrations remembering the birth of Jesus were going on in full swing at the Catheral Chapel.
#  The Event Management Team had arranged for some exciting games after the mass worship and feast, where adults and kids of 
# all ages
#  participated very actively.
#  "Chocolate Game" was organized for the kids which involved a standard chocolate of n by m pieces.
#  More formally, chocolate is a rectangular plate consisting of n rows and m columns.
#  Two kids at a moment will play with the chocolate. First kid takes the chocolate and cuts it into two parts by making either
#  a horizontal or vertical cut.
#  Then, the second kid takes one of the available pieces and divides into two parts by either making a horizontal or vertical cut.
#  Then the turn of first kid comes and he can pick any block of the available chocolates and do the same thing again.
#  The player who cannot make a turn loses.
#  Write a program to find which of the kids will win if both of them play optimally. Output "Yes", if the kid who 
# plays first will win, otherwise print "No".

#  Input Format:
#  The only line of the input contains two space separated integers n and m - the sizes of the chocolate.

#  Output Format:
#  Output a single line containing one word "Yes" (without quotes) if there is a sequence of moves leading to the winning of the
#  person who moves first and "No" (without quotes) otherwise.
#  Refer sample input and output for formatting specifications.

#  Sample Input 1:
#  1 2

#  Sample Output 1:
#  Yes

#  Sample Input 2:
#  1 3

#  Sample Output 2:
#  No
# '''
n,m=[int(i) for i in input().split()]

for i in range(n*m):
    a=n*m/2
    b=a/2

    if(a==1):
        print("Yes")
        break
    else:
        print("No")    
        break
