n=int(input('Filas'))
for i in range(n):
    a = ''
    for j in range(n):

        if j>=i:
            a+='* '
        else:
            a+=' '

    print(a)