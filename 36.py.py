n1=float(input("Digite el primer número: "))
n2=float(input("Digite el segundo número: "))
n3=float(input("Digite el tercer número: "))
x=n1+n2
if x==n3:
    print("La suma es igual al tercer número.")
else:
    if x>n3:
        print("La suma es mayor al tercer número.")
    else:
        print("La suma es menor al tercer número.")