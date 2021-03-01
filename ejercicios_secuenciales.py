# Punto1
p1 = float(input('Digite la cantidad de dinero que invirtio la persona 1'))
p2 = float(input('Digite la cantidad de dinero que invirtio la persona 2'))
p3 = float(input('Digite la cantidad de dinero que invirtio la persona 3'))
total = p1 + p2 + p3
porc1 = (p1 / total) * 100
porc2 = (p2 / total) * 100
porc3 = (p3 / total) * 100
print(f'El total fue de {total}')
print(f'El porcentaje de la persona 1 es de {porc1}%, de la persona 2 es de {porc2}% y de la persona 3 es de {porc3}%')
# Punto2
salar = float(input('Digite el salario del empleado'))
hijos = float(input('Digite la cantidad de hijos'))
bonif = hijos * 80000
total = salar + bonif 
print(f'El total a pagar es de ${total}')
# Punto3
saldin = float(input('Digite el saldo'))
interes = saldin * 0.015
saldfin = saldin + interes
print(f'El saldo final es de ${saldfin}')
# Punto4
metros = float(input('Digite los metros cuadrados del terreno'))
tot = metros * 80000
cuotain = tot * 0.35
cuotares = tot * 0.65
cuotadiv = cuotares / 12
print(f'El total a pagar es de ${tot}, con una cuota inicial de ${cuotain} y 12 cuotas de ${cuotadiv}')
# Punto5
sueldo = float(input('Digite el sueldo'))
ley = sueldo * 0.01
seguroso = sueldo * 0.04
segurofor = sueldo * 0.005
caja = sueldo * 0.05
tot = sueldo - (ley + seguroso + segurofor + caja)
print(f'El descuento de ley es de {ley}')
print(f'El descuento de seguro social es {seguroso}')
print(f'El descuento de seguro forzoso es {segurofor}')
print(f'El descuento de caja es {caja}')
print(f'El total es {tot}')
# Punto6
color = float(input('Digite la cantidad de colores '))
palabras = float(input('Digite la cantidad de palabras '))
centimetros = float(input('Digite la cantidad de centimetros'))
total = (color * 25000) + (centimetros * 15000) + (palabras * 20000)
print(f'El total a pagar es: ${total}')

# Punto7
años = int(input('Digite la cantidad de años '))
pago = 0
for i in range(años):
    if i == 0:
        pago = pago + 100000
    else:
        pago = pago + 120000

print(f'El profesor ha trabajado por {años} años por lo tanto su pago es de: ${pago}')
# Punto8
hora = float(input('Digite la cantidad de horas '))
pag = 20000 * hora
desc = pag * 0.05
tot = pag - desc
print(f'El monto total a pagar al profesor es de ${tot}')

# Punto9
minicial = float(input('Digite el monto inicial '))
mfinal = float(input('Digite el monto final '))
costo = minicial - mfinal
recarga = costo * 0.20
tot = costo + recarga
print(f'El costo de la llamada con recarga es de : {tot}')
# Punto10
foto = float(input('Digite la cantidad de fotos a revelar'))
monto = 1500 * foto
iva = monto * 0.16
tot = monto + iva
print(f'El total a pagar es: ${tot}')
# Punto11
presupuesto = float(input('Digite el presupuesto anual '))
gin = presupuesto * 0.40
traum = presupuesto * 0.30
pedia = presupuesto * 0.30
print(f'Repartiendo el presupuesto de acuerdo a sus porcentajes: A ginecologia le corresponde ${gin}, traumatologia le corresponde ${traum} y a pediatria le corresponde ${pedia}')
# Punto12
dias = int(input('Digite la cantidad de dias de alquiler'))
dvd = int(input('Digite la cantidad de dvd a alquilar '))
tot = (dvd * 1500) * dias
print(f'El total a pagar es de ${tot} debido a que alquilo {dvd} pelicuas para {dias} dias')

# Punto13
dias = int(input('Digite la cantidad de dias del tour '))
personas = int(input('Digite la cantidad de personas del tour '))
monto = (25000 * personas) * dias
print(f'La cantidad total a pagar es : {monto} ')

# Punto14
dias = int(input('Digite la cantidad de dias '))
pago = 0
for i in range(dias):
    if i == 0:
        pago = pago + 100000
    else:
        pago = pago + 200000
print(f'El total a pagar es de ${pago} por la estadia de {dias} dias')

# Punto15
prestamo = float(input('Digite la cantidad del prestamo '))
interes = prestamo * 0.24
total = prestamo + interes
mitad = total / 2
cespecial = mitad / 4
cordinaria = mitad / 20
print(f'El total a pagar es de ${total}, se pagara 4 cuotas especiales de ${cespecial} y 20 de ${cordinaria}')
    

