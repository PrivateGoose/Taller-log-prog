x=""
n=int(input("Digite un número: "))

for i in range (n):
    for w in range (i+1):
        x=x+"@"
    x=x+"\n"
print(x)