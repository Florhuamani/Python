# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad:int=int(input("ingrese su edad:"))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas .

contraseña="contraseñasegura123"
contraseña_usuario=input("ingresa tu contraseña:")

# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
numero=int(input("introduce un numero entero positivo:"))
if numero < 0:
    print("por favor, introduce un numero entero positivo.")
else:
    for i in range (numero, -1, -1 ):
        if i == 0 :
            print(i, end="")
        else:
            print(i, end=",")
            
