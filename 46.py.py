n1=float(input("Digite el primer número: "))
n2=float(input("Digite el segundo número: "))
n3=float(input("Digite el tercer número: "))
if n1==n2 or n1==n3:
    print("Hay al menos dos números iguales.")
else:
    if n2==n3:
        print("Hay al menos dos números iguales.")
    else:
        print("Todos los números son diferentes.")