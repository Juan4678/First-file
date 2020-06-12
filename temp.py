#Debugger

#Tipos de bugs

'''Error de sintaxis- Este tipo de bug viene de errores de tipografía. Cuando el interpretador de Python ve un error de sintaxis,
es porque tu código no está escrito en el lenguaje apropiado de Python. Un programa de Python aún con un error de sintaxis no correrá.'''

'''Error de tiempo de ejecución- Estos ocurren cuando el programa está corriendo. El programa trabajará hasta que alcance la línea
del código con el error, y entonces el programa acabará con un mensaje de error (llamado crashing). El interpretador de Python
mostrará un Traceback: un mensanje de error mostrando la línea con el problema. '''

'''Error semántico- Estos erros (los más difíciles de arreglar) no paran el programa, pero evitan que el programa haga lo que
el programador pretendía que hiciera. Por ejemplo, si el programador quiere que la variable total sea la suma de los valores
de las variables a,b y c, pero escribe total= a*b*c, entonces el valor en total estará mal. Esto podría detener después el programa,
pero no será inmediatamente obvio dónde ocurrió el error semántico.'''

#Example of a code without bugs
import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
   if random.randint(0, 1) == 1:
        heads = heads + 1
   flips = flips + 1

   if flips == 900:
         print('900 flips and there have been ' + str(heads) + ' heads.'
             
   if flips == 100:
         print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
       
   if flips == 500:
         print('Halfway done, and heads has come up ' + str(heads) +
              ' times.')
print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
print('Were you close?')
