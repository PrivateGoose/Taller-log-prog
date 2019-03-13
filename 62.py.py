suma=0
n=int(input("Digite el primer valor: "))
m=int(input("Digite el segundo valor: "))
if m<n:
    print("No se puede desarrollar lo pedido")
else:
    for i in range(n,m+1):
        suma = i+i
print(suma)