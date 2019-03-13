import cmath

a=float(input("Digite el valor de a: "))
b=float(input("Digite el valor b: "))
c=float(input("Digite el valor c: "))
d = (b**2)-(4*a*c)
solu1=(-b-cmath.sqrt(d))/(2*a)
solu2=(-b+cmath.sqrt(d))/(2*a)
print("La solución para esta funcion es {} y {}.".format(solu1,solu2))