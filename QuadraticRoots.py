from math import sqrt
print("Enter values of a, b and c to find roots of quadratic equation ax^2+bx+c=0")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=(b*b-4*a*c)
if s<0:
    print("Roots of given quadratic equation are,"+str((-b-sqrt(abs(s)))/2*a)+"i and "+str((-b+sqrt(abs(s)))/2*a)+"i")
elif s>0:
    print("Roots of given quadratic equation are,"+str((-b-sqrt(s))/2*a)+" and "+str((-b+sqrt(s))/2*a))
else:
    print("Roots are repeated and value is. "+str(-b/(2*a)))
