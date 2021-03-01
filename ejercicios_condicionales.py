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
# Punto5
precio = float(input('Digite el precio del automovil o terreno'))
auto = precio
terreno = precio
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

# Punto9
n1 = float(input('digite el numero 1 '))
n2 = float(input('digite el numero 2 '))
if n1 == n2:
    mult = n1 * n2
    print(f'Son iguales y al multiplicarlos el resultado es: {mult}')
else:
    if n1 > n2:
        res = n1 - n2
        print(f'El numero 1 es mayor que el numero 2 y al restarlos el resultado es: {res}')
    else:
        sum = n1 + n2
        print(f'El numero 2 es mayor que el numero 1 y al sumarlos el resultado es: {sum}')
# Punto10
n1 = float(input('digite el primer numero '))
n2 = float(input('digite el segundo numero '))
n3 = float(input('digite el tercer numero '))
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