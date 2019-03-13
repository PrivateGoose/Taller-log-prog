decimal=0
binario=input("Digite un número binario: ")
for digito in binario:
    decimal=decimal*2 + int(digito) 
print("La conversión da: {} .".format(decimal))