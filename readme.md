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
3. No crear código usando ChatGPT. Pueden estudiar o practicar con este, pero por supuesto nada de copiar y pegar el código.
## Distribución
- Martín Ezequiel Monzón: 

## Miembros
- <b>Facundo Bellochi</b>
- <b>Maximiliano Duarte</b>
- Martín <b>Ezequiel Monzón</b>