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
    

