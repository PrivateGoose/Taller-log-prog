a=int(input("Digite un año: "))
if a%4==0:
    if a%100 != 0 or a%400==0:
        print("El año {} es biciesto.".format(a))
    else:
        print("El año {} no es biciesto.".format(a))