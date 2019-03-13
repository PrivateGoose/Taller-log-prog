x1=int(input("Digite un valor positivo en x para su primera coordenada: "))
y1=int(input("Digite un valor positivo en y para su primera coordenada: "))
x2=int(input("Digite un valor positivo en x para su segunda coordenada: "))
y2=int(input("Digite un valor positivo en y para su segunda coordenada: "))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5
print("La distancia entre sus coordenadas es de: {}".format(d))