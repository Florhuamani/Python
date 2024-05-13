# ejemplo de for
# imprimir los números pares 
# entre el 1 - 20

for n in range (1 , 21):
    if n%2==0:
        print(n)

#crear un programa que me imprima las 5 vocales :
vocales ="aeiou"
for n in range(0,5):
    print(vocales[n])
 #crear un programa que me muestre los primeros 8 numeros pares:
contador=0
for n in range(1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es par numero {contador}")
   
# crear un programa que pida al usuario escribir una oración y mostrar por terminal la cantidad de vocales "a" que tiene esa oración.
#OJO: SOLO LAS "a" MINÚSCULAS.
oracion:str=input("escriba una oracion:")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador+=1
print(f"la cantidad de letras a que tengo es {contador}")

#crear un programa que me cuente la cantidad de comas y me muestre sus índices.
#OJO: Tienes que pedir al usuario.
oración:str=input("escriba una oración:")
contador=0
for 


# ejemplo de if - else 
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")

edad_dos:int=int(input("escribe tu edad:"))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)


