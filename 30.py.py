a=float(input("Digite el valor de su compra: "))
if a>150000:
  desc=a*0.05
  desc2=a-desc
  print("Por compra al ser mayor de 150.000 se le aplicará un descuento del 5%")
  iva=desc2*0.19
  iva2=desc2+iva
  print("El valor de su compra es de: ${}, le queda en: {} y con el iva queda en: ${}".format(a,desc2,iva2))
else:
  vent=a*0.19
  vent2=a+vent
  print("El valor de su compra es de: ${} y con iva le queda en: ${}".format(vent,vent2))