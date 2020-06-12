#Este es un juego de adivinar el n√∫mero

import random

Intentos=0
print("Hola, øcÛmo te llamas?  ")
nombre=input()

numero= random.randint(1,20)
print("Bueno,", nombre, "estoy pensando en un numero entre 1 y 20")

for Intentos in range (6):
    print("adivina")  #cuatro espacios en frente de "print"
    intento=input()
    intento=int(intento)
    
    if intento < numero:
        print("tu numero es menor a la respuesta") #8 esoacios en frente de "print"
        
    if intento > numero:
        print("tu n√∫mero es mayor a la respuesta")
    
    if intento==numero:
        break
    
if intento == numero:
    Intentos = str(Intentos +1)
    print("Bien hecho", nombre, ", adivinaste el numero en", Intentos, "intentos")

if intento != numero:
    numero=str(numero)
    print("No, el numero en que pensaba era", numero,".")
    