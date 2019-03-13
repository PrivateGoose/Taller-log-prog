b=input("Digite el nombre de usuario: ")
a=int(input("Digite la contraseña: "))
c=str("usuario.2019@gmail.com")
d=str("contraseña")
f=0
if b!=c or a!=d :
    while e<1:
        a = int(input("Contraseña incorrecta: "))
        b= input("Usuario incorrecto: ")
        f+=1
        if f>3:
            break
else:
    if b==c and a==d:
        print("Login succesful")

if f>3:
    print("Límite máximo de intentos alcanzado")