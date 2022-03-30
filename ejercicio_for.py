diccionario = {"Daniel" : 1, "Francisco" : 5, "Laura" : 24, "Ines" : 45}
for i,j in diccionario.items():
    print("{0} escogio el número {1}".format(i,j))

print("-----------------")
i=0
j=0
for i,j in diccionario.items():
    a=j
    if j>a:
        a = j
print ("El numero mayor es: ",a)
