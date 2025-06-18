# Proyecto de Permutaciones, Combinaciones y Variaciones (utilizando Python)
Este proyecto en python permite generar y mostrar:
- Todas las **permutaciones** posibles de un conjunto de elementos.
- Todas las **combinaciones** posibles dentro de un subconjunto de tamaño "r"
- Todas las **variaciones** posibles (ordenadas, duh) de un subconjunto de tamaño "r"

## Pseudocódigo de  guía:
```
  función principal/main:
    Mostrar menú de opciones
    Pedir al usuario los elementos separados por coma
    Si la opción requiere r (combinación o variación), pedir r
    Ejecutar la operación correspondiente
    Mostrar los resultados

  funcitón factorial(paramétro: number):
    Si number es 0 o 1: retornar 1
    Sino: retornar number * factorial(number-1)
  
  funcion quitarAcentos/removeAccents:
    Crear un objeto con todas las alternativas posibles, incluyendo ñ y ü, ë, ï, ö, o acento alterno (à, è, ì, ò, ù)
  
  funcion permutaciones(parametro: lista):
    si la longitud de la lista es 1: retornar [lista]
    para cada índice de i en la lista:
      tomar el elemnto i
      Formar una lista con los elementos restantes
      Recursivamente obtener permutaciones del resto
      agregar el elemento actual al principio de cada permutación
    Retornar la lista completa de permutaciones
  
```

## REGLAS
1. No utilizar librerías externas. <br>
  Esto puede parecer algo contraproducente, pues, las librerías nos ahorrarán mucho trabajo.
  Sin embargo, tenemos que tener en cuenta que somos un grupo de 3 personas para hacer un trabajo que es medianamente simple en Python. Además, a la hora de practicar hay que recordar qeu es un ejercicio académico útil para comprender los principios de conteo.

2. Las variables, funciones y cualquier tipo de contenido nombrable, **asignarlas en inglés**
3. No crear código usando ChatGPT (u alguna otra variante en IA). Pueden estudiar o practicar con este, pero por supuesto nada de copiar y pegar el código.


## Ejemplo
> ¿Cómo debería ser el flujo?
```
Escenario 1:
  Operaciones disponibles:
  1. Permutaciones (Todas las ordenaciones posibles)
  2. Combinaciones (Las selecciones sin importar el orden)
  3. Variaciones (Selecciones donde el orden importa)
  Por favor, ingrese una opción (numérica o por nombre): <input> 1
  escogiste permutación
  Por favor, introduzca los elementos, separados por coma. (por ejemplo: a,b,c)

  Permutaciones (6 en total):
  ['a', 'b', 'c']
  ['a', 'c', 'b']
  ['b', 'a', 'c']
  ['b', 'c', 'a']
  ['c', 'a', 'b']
  ['c', 'b', 'a']
Escenario 2:
Ingrese una opción (1-3): 2
escogiste combinación
Por favor, introduzca los elementos, separados por coma. (por ejemplo: a,b,c): <input> a,b,c,d
¿Cuántos elementos desea tomar? <input> 2

Combinaciones de 2 elementos (6 en total):
['a', 'b']
['a', 'c']
['a', 'd']
['b', 'c']
['b', 'd']
['c', 'd']

Escenario 3:
escogiste variación
Por favor, introduzca los elementos, separados por coma. (por ejemplo: a,b,c): <input> x,y,z
¿Cuántos elementos desea tomar? <input> 2

Variaciones de 2 elementos (6 en total):
['x', 'y']
['x', 'z']
['y', 'x']
['y', 'z']
['z', 'x']
['z', 'y']
```

## Miembros
- <b>Facundo Bellochi</b>
- <b>Maximiliano Duarte</b>
- Martín <b>Ezequiel Monzón</b>

## Distribución
- Martín Ezequiel Monzón: **Permutacione**s
- Facundo Bellochi: **Combinaciones**
- Maxi Duarte: **Variaciones**
