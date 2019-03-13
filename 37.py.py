distancia=float(input("Digite la distancia que recorrerá (En KM) "))
dias=float(input("Por favor ingrese el número de dias a viajar: "))
precio=5000*distancia
if distancia>1000 and dias>7:
    x=precio-(precio*0.15)
    print("Se hará un descuento del 15% haciendo que su viaje de ${} cueste ahora ${}.".format(precio,x))
else:
    print("El valor total es de: ${}.".format(precio))