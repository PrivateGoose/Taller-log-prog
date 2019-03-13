n1=float(input("Digite su primera nota: "))
n2=float(input("Digite su segunda nota: "))
n3=float(input("Digite su tercera nota: "))
n4=float(input("Digite su cuarta nota: "))
n5=float(input("Digite su quinta nota: "))
n1p=n1*0.15
n2p=n2*0.2
n3p=n3*0.15
n4p=n4*0.3
n5p=n5*0.2
prom=n1p+n2p+n3p+n4p+n5p
print("Su promedio es de: {}".format(prom))
if prom<3:
  print("Reprobó la asignatura")
else:
  if prom>=3 and prom<4.5:
    print("Aprobó la asignatura")
  else:
    
    if prom>4.5:
      print("Felicitaciones, está aprobando la asignatura por encima de 4.5")