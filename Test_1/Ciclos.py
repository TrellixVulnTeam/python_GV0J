manzanas = 10

while manzanas > 0:
    print("Me estoy comiendo una manzana #" + str(manzanas))
    manzanas-=1
 
print("Me quede sin manzanas")

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in lista_numeros:    
    if numero == 3:
        continue
    print(numero)

vocales = "aeiou"
 
for vocal in vocales:
    print(vocal.upper())