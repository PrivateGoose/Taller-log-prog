n1=int(input("Digite el primer número: "))
n2=int(input("Digite el segundo número: "))
n3=int(input("Digite el tercer número: "))
if n1>n2>n3:
    print("El número mayor es {} y el menor es {}.".format(n1,n3))
else:
    if n1>n3>n2:
        print("El número mayor es {} y el menor es {}.".format(n1,n2))
    else:
        if n2>n1>n3:
            print("El número mayor es {} y el menor es {}.".format(n1,n3))
        else:
            if n2>n3>n1:
                print("El número mayor es {} y el menor es {}.".format (n2,n1))
            else:
                if n3>n1>n2:
                    print("El número mayor es {} y el menor es {}.".format(n3,n2))
                else:
                    if n3>n2>n1:
                        print("El número mayor es {} y el menor es {}.".format(n3,n1))