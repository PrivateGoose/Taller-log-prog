n1=float(input("Digite el primer número: "))
n2=float(input("Digite el segundo valor: "))
n3=float(input("Digite el tercer valor: "))
if n1>n2>n3 or n1>n3>n2:
    print("El {} es el mayor de todos.".format(n1))
else:
    if n2>n1>n3 or n2>n3>n1:
        print("El {} es el mayor de todos.".format(n2))
    else:
        if n3>n1>n2 or n3>n2>n1:
            print("El {} es el mayor de todos.".format(n3))