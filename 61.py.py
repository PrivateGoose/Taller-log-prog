n=int(input("Digite el primer número: "))
m=int(input("Digite el segundo número: "))
if m<n:
    print("Es imposible desarrollar lo pedido")
else:
    for i in range(n,m):
        i=i+1
        print("Los números entre {} y {} es : {}.".format(n,m,i))