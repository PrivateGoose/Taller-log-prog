a=int(input("Digite un número: "))
if a < 100000:
    print("El número total de digitos es: ",len(str(abs(a))))
else:
    print("Solo se pueden analizar números menores a 100000.")