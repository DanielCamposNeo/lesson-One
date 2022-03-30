
dato = float(input("Introduce una cantidad"))
acumulado = 0

while dato != 0:
    if dato < 0:
        print("Cantidad no valida")
        break
    else:
        acumulado += dato
        dato = float(input("Introduce una cantidad"))
if acumulado > 1000:
    acumulado -= acumulado * 0.1

print ("El total a pagar es :", acumulado)
