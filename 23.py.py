a=int(input("Digite la cantidad de segundos: "))
hora=int(a/3600)
c=a%3600
minu=int(c/60)
seg=c%60
print("{}:{}:{}".format(hora,minu,seg))