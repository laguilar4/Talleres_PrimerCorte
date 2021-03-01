import random
# Punto1
cantidad = float(input('digite la cantidad de camisas a comprar '))
precio = float(input('digite el precio de las camisas '))
total = cantidad * precio
if cantidad >= 3:
    desc = total * 0.3
    res = total - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')
else:
    desc = total * 0.1
    res = total - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')

# Punto2
tot = float(input('digite el total a pagar de la compra '))
nazar = random.uniform(0, 100)
print(f'El numero al azar escogido es: {nazar}')
if nazar < 74:
    desc = tot * 0.15
    res = tot - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')
else:
    desc = tot * 0.2
    res = tot - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')

# Punto3
mont = float(input('Digite el monto por el que se efectua la fianza'))
cuota = float(input('Digite la cantidad de cuotas'))
if mont < 50000:
    porc = mont * 0.03
    tot = mont + porc 
    res = tot / cuota
    print(f'Cada cuota sera de: ${res}')
    print(f'El monto total es: ${tot}')
else:
    porc = mont * 0.02
    tot = mont + porc 
    res = tot / cuota
    print(f'Cada cuota sera de: ${res}')
    print(f'El monto total es: ${tot}')

# Punto4
acumpu = 0
acumga = 0
for i in range(5):
    ganancias = float(input(f'Digite las ganancias del dia: {i} '))
    puntos = float(input(f'Digite los puntos del dia: {i} '))
    acumpu = acumpu + puntos
    acumga = acumga + ganancias
promedio = acumpu / 5
print(f'El promedio de puntos es: {promedio}')
if promedio > 170:
    multa = acumga / 2
    print(f'Debe pagar una multa de: {multa}')
else: 
    print('No debe pagar multa')


# Punto5
precio = float(input('Digite el precio del automovil o terreno'))
vidautila = float(input('Digite la vida util del automovil'))
incre = float(input('Digite el incremento anual en porcentaje del terreno(Escribirlo en decimal) '))
depreca = (precio / vidautila) * 3
deprect = (precio * incre) * 3
print(f'La depreciacion del auto es: {depreca}')
print(f'La depreciacion del terreno es: {deprect}')
mitad = deprect / 2
if depreca < mitad:
    print('Se comprara el automovil')
else:
    print('Se comprara el terreno')

# Punto6
cantcom =  float(input('digite la cantidad de computadores a comprar '))
totapagar = cantcom * 11000
if cantcom < 5:
    desc = totapagar * 0.1
    res = totapagar - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')
elif cantcom >= 5 and cantcom < 10:
    desc = totapagar * 0.2
    res = totapagar - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')
else:
    desc = totapagar * 0.4
    res = totapagar - desc
    print(f'El total a pagar con descuento es: ${res}')
    print(f'La cantidad de dinero que ahorro es de: ${desc}')
# Punto7
prec = float(input('Digite el precio del producto a comprar'))
marca = str(input('Digite la marca del producto '))
if prec >= 2000:
    desc = prec * 0.1
    tot = prec - desc 
    if marca == "NOSY":
        desc2 = prec * 0.05
        tot2 = tot - desc2
        iva = prec * 0.16
        res = tot2 + iva
        print(f'El precio con descuento de marca e iva es: {res}')
    else:
        iva = prec * 0.16
        res = tot + iva
        print(f'El precio sin descuento de marca y con iva es: {res}')
else:
    if marca == "NOSY":
        desc2 = prec * 0.05
        tot2 = prec - desc2
        iva = prec * 0.16
        res = tot2 + iva
        print(f'El precio con descuento de marca e iva es: {res}')
    else:
        iva = prec * 0.16
        res = prec + iva
        print(f'El precio sin descuento de marca y con iva es: {res}')

# Punto8
montotal = float(input('Digite el monto total de la compra '))
if montotal > 500000:
    propio = montotal * 0.55
    banco = montotal * 0.30
    credito = montotal * 0.15
    fabr = credito * 0.20
    print(f'La empresa pagara de su dinero {propio}, pedira prestado del banco {banco}, se pagara con credito {credito} y el interes por credito es{fabr}')
else:
    propio = montotal * 0.70
    credito = montotal * 0.30
    fabr = credito * 0.20
    print(f'La empresa pagara de su dinero {propio}, se pagara con credito{credito} y el interes por credito es {fabr}')
# Punto9
n1 = float(input('Digite el numero 1 '))
n2 = float(input('Digite el numero 2 '))
if n1 == n2:
    mult = n1 * n2
    print(f'Son iguales y al multiplicarlos el resultado es: {mult}')
else:
    if n1 > n2:
        res = n1 - n2
        print(f'El numero 1 es mayor que el numero 2 y al restarlos el resultado es: {res}')
    else:
        suma = n1 + n2
        print(f'El numero 2 es mayor que el numero 1 y al sumarlos el resultado es: {suma}')
# Punto10
n1 = float(input('Digite el primer numero '))
n2 = float(input('Digite el segundo numero '))
n3 = float(input('Digite el tercer numero '))
if n1 > n2:
    if n1 > n3:
        print(f'El mayor es el numero: {n1}')
    else:
        print(f'El mayor es el numero: {n3}')
else:
    if n2 > n3:
        print(f'El mayor es el numero: {n2}')
    else:
        print(f'El mayor es el numero: {n3}')