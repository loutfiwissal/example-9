from math import*
A=int(input("please enter the value of A:" ))
B=int(input("please enter the value of B:" ))
C=int(input("please enter the value of C:" ))
D=(B*B)-4*A*C
if D<0 :
    print("no solution")
elif D==0 :
    print("the solution is:",-B/(2*A))
else :
    x1=(-B-sqrt(D))/(2*A)
    x2=(-B+sqrt(D))/(2*A)
    print("the solutions are:",x1,",",x2)
