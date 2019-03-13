print("Digite el peso de cada uno de sus bultos, si no tiene mas, por favor poner 0")
c=int(input("Bultos que va a ingresar: "))
cont1=0
cont2=0
bultos=0
pesoTotal=0
valorTotal=0
for i in range(0,c):
    a=float(input("ingresar peso"))
    if i==0 and a<500:
       cont1=a
       cont2=a
    if a < cont2 and a!=0 :
            cont2 = a
    if a>cont1 and a<501:
            cont1=a
    if a!=0 and a>0 and a<=25:
            bultos+=1
            pesoTotal=pesoTotal+a
    if a!=0 and a>25 and a<=300:
            bultos+=1
            pesoTotal=pesoTotal+a
            valorTotal=valorTotal+(a*1500)
    if a!=0 and a>300 and a<=500:
        bultos+=1
        pesoTotal=pesoTotal+a
        valorTotal=valorTotal+(a*2500)
    if a>500 :
        print("Este bulto no será embarcado en el avion por exceso de peso")
    if a==0 :
        break
if pesoTotal>1800:
     print("no podemos subir esto al avion por que su peso es: {}, El peso debese menor o igual a 1800".format(pesoTotal))
else:
 if pesoTotal <=1800:
    print("el numero total de bultos es: {}".format(bultos))
    print("El peso del bulto mas pesado es {} \nEl bulto menos pesado es: ".format(cont1,cont2))
    print("El peso promedio de peso cada bulto es", (pesoTotal / bultos))
    print("El precio de el total de bultos en pesos Colombianos es: {}".format(valorTotal))
    print("El valor por peso en dolares será: ", (valorTotal * 3165))
    print("El  valor por peso de los bultos en pesos Colombianos es de: {}".format)