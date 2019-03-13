mayor=0
menor=0
igual=0
n=int(input("Digite la cantidad de números: "))
m=int(input("Digite el segundo valor: "))
for num in range(n,m+1):
	if num>100:
		mayor+=1
	elif num==100:
		igual+=1
	else:
		menor+=1
print("Hay {} numeros mayores a 100.".format(mayor))	
print("Hay {} números menores a 100.".format(menor))			
print("Hay {} números iguales a 100.".format(igual)) 