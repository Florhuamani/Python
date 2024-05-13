# CONTROLES DE FLUJO
Todos los programas trabajan a traves de instrucciones ordenadas. Existe maneras de romper con el flujo normal de los programas creando `bifurcaciones` o creando `repetición` de instrucciones.
## Decisiones 
> La sentencia if 
La sentencia de decisión en python es `if`. En su escritura debemos añadir una **expresión de comparación** terminando con `:` al final de la línea.
> ejemplo:
```python
if true:
    print("es verdad")
```
> Else -elif
### primer ejemplo de if estructurado:
```python
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
```
## segundo ejemplo if almacenado en variable:
```python
edad_dos:int=int(input("escribe tu edad:"))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)
```

# ciclos
son los controles de flujoque repiten código y su sintaxis es la siguiente
> Para FOR:

```PYTHON
# este codigo imprime los números
# del 1 al 10
for n in range(1,11):
    print(n)
```
> Para while:
