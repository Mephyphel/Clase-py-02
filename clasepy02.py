
""" print(type("1"))
print("1")

print(type("hola mundo"))
print("hola mundo")

print(type(1))
print(1)

carro = 5
numero = "carro"
texto = "1"
numero_direccion = 524
piso_casa=1

print(type(numero))
print(numero)

print(type (texto))
print(texto)

print("la suma es :", numero+numero)

print("El reporte del formulario es  :", numero_direccion+piso_casa)
 """
factura={"pan","huevos", 100, 1234, "mimundo", "ggg", 1223, "5425525"}
print(factura)

factura.add("hola")

print(factura)
#["pan", "huevos", 100, 1234, "mimundo", "ggg", 1223, "5425525", "revisando", 12324]

factura2=factura.copy()

factura2.add("object")

print(factura2)
print(factura)