#Tipos de datos

#DATO NONE:

n= ()
print(type(n))

#datos numéricos:
num = 2.5
print (type(num))   #float
num = 5
print (type(num))   #int
num = 6+9j
print (type(num))   #complex
a = 5.6 
b = int(a)          #convertir un float a un int
print (type(b))
print (b)
k = float(b)        #convertir un int a un float 
print(type(k))
print (k)
k = 6
c = complex(b,k)    #convertir a número complejo
print (type(c))
print(c)
bool = b<k          #núm.booleano, indica una condición, si es verdad o falso.
print (type(bool))
print (bool)
bool = b>k          
print (type(bool))
print (bool)
print (int(True))
print (int(False))


#DATOS DE SECUENCIA:
#datos de lista:

lst = [25, 36, 45, 12]
print (type(lst))

#datos set:

s = {25, 36, 45, 15, 12, 25}
print (s)
print (type(s))

#datos tuple

t = (25, 36, 4, 57, 12)
print (t)
print (type(t))

#datos string

str = "juan"
print (str)
print (type(str)) 
st= "a"
print (st)
print (type(st))

#datos range

range(10)
print (list(range(10)))
print(list(range(2,10,2)))
print(type(range(10)))

#DATOS DE DICCIONARIO

d= {'juan':'Iphone X', 'romeo':'xiaomi', 'alonso':'Iphone 11'}
print (d)
print (d.keys())
print (d.values())
print (d['romeo'])
print (d.get('alonso'))













