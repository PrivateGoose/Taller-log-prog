n=int(input("Digite un número para hacer una secuencia: "))
for i in range(1,n+1):
	if i%2==0:
		i=i*-1
	print(i)