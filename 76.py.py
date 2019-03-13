cont=0
a=int(input("Digite un número: "))
b=1
while b<a+1:
    if a%b==0:
        print("Con este numero la division es exacta: {} ".format(b))
        cont+=1
    b+=1
print("la cantidad de factores que tiene son: {} ".format(cont))