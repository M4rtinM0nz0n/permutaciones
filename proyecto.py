
print('=== Equipo === \nMartín Monzón, Maximiliano Duarte, Facundo Bellochi')
"""
  Esto es una función recursiva, para entender cómo funciona esto, hay que entender algo llamado Callstack.
  Un callstack es como un listado de llamadas a funciones. Imaginemos que tenemos un prorgama que simula un restaurante.
  Dentro de este restaurante, los 
"""
def factorial(number):
  if number <= 1:
    return 1
  return number * factorial(number - 1)

def showMenu():
  pass

"""
  Esta función la creé (Yo, Martín Ezequiel Monzón) con el propósito de remover acentos y reducir el margen de error.
  Por ejemplo, ¿Qué pasa si cuando el usuario va a seleccionar una opción, pone acento? Pero nosotros escribimos el control de flujo SIN acentos.
  Por ejemplo (in pseudocódigo plis):
    if option = permutacion:
      resolver permutacion...
    else if option = combinacion:
      resolver combinacion...
    else if option = variacion:
      resolver variacion...
    else:
      print(Por favor, introduzca un valor válido.)
    
    Esto siempre devolverá el else case. Hay que recordar que, en la programación, a los usuarios hay que tratarlos como lo más estúpido posible.
    Es decir, si le damos un vaso al usuario, hay que esperar que el trate de tomarlo por debajo en lugar de arriba.
    Aunque todos sepamos cómo beber de un vaso, siempre va a haber alguien que nos sorprenda. (Esto es un caso extremo, pero sirve para ejemplificar).

  La función recibe: un String
  dentro hay un objeto (o diccionario) que cuenta con las alternativas de acento.
  Itera (recorre) sobre el string y compara cada letra.
  Además, al final, devuelve el string en lowercase (minúscula), pues, de todos modos siempre utilizaremos minúsculas y es mejor eso a tener que preparar un base case para:
    Permutacion
    Permutación
    Permutaciones
    permutacion
    permutación
    permutaciones
    etc...
  Ejemplo de uso:
    str original = áéíóúÁÉÍÓÚ
    str devuelto = aeiouaeiou
  
  Cabe recalcar que, para otros tipos de acentos como ü (con los dos puntitos arriba, no tengo idea de cómo se llamará, lol) y para la ñ
  También devuelve sus variantes sin acento (ü = u y ñ = n). Lo mismo con los acentos alternos (à = a)
  Esto por si a algún gracioso se le ocurre escribir:
    permutacioñes
"""
def removeAccents(string):
  accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ñ': 'n',
    }
  
  textWithoutAccents = ''
  for c in string:
    textWithoutAccents += accents.get(c, c)
  return textWithoutAccents.lower()

def verifyOption(option):
  availableOptions = ['permutacion', 'combinacion', 'variacion']
  # Transformamos el número a entero.
  try:
    option = int(option)
  except ValueError:
    pass

  if isinstance(option, int):
    if(option > 2):
      return 404
    return availableOptions[option - 1]
  elif isinstance(option, str):
    option = removeAccents(option)
    if option in ['permutacion', 'permutaciones']:
      return 'permutación'
    elif option in ['combinacion', 'combinaciones']:
      return 'combinación'
    elif option in ['variacion', 'variaciones']:
      return 'variación'
    else:
      return 404
  else:
    print("Error, ocurrió un escenario inesperado, valor inválido.")

def solvePermutation(elements):
  if len(elements) == 1:
    return [elements]
  perms = []
  for x in range(len(elements)):
    remaining = elements[:x] + elements[x+1:]
    for p in solvePermutation(remaining):
      perms.append([elements[x]] + p)
  return perms

def solveCombination(elements, r):
  def combine(current, remaining, start):
    if len(current) == r:
      result.append(current[:])
      return
    for i in range(start, len(remaining)):
      current.append(remaining[i])
      combine(current, remaining, i + 1)
      current.pop()

  result = []
  combine([], elements, 0)
  return result

def main():
  print("Operaciones disponibles: " \
        "\n1. Permutaciones (Todas las ordenaciones posibles)" \
        "\n2. Combinaciones (Las selecciones sin importar el orden)" \
        "\n3. Variaciones (Selecciones donde el orden importa)")
  option = input("Por favor, ingrese una opción (numérica o por nombre): ")
  option = option.lstrip('0');
  option = verifyOption(option)
  if(option == 404):
    print('Error, introduzca, por favor, una operación adecuada.')
    print('¿Quiere volver a intentarlo?')
    tryAgain = input('si/no: ')

    if removeAccents(tryAgain) == 'si' or removeAccents(tryAgain) == 's':
      return main()
    else:
      return '¡Nos vemos!'

  print(f"escogiste {option}")

  elements = input('Por favor, introduzca los elementos, separados por coma. (por ejemplo: a,b,c): ')
  elements = elements.replace(" ", "").split(',')
  if removeAccents(option) == "permutacion":
    res = solvePermutation(elements)
    print(f"\nPermutaciones ({len(res)} en total):")
    for r in res:
      print(r)
  
  elif removeAccents(option) == "combinacion":
    r = int(input("¿Cuántos elementos desea elegir? "))
    if r > len(elements) or r <= 0:
      print("Número inválido. No puede elegir más elementos de los disponibles.")
      return
    res = solveCombination(elements, r)
    print(f"\nCombinaciones ({len(res)} en total):")
    for c in res:
      print(c)
  elif removeAccents(option) == "variacion":
    return "No implementado"

"""
  ------- Nota -------
  Esto es una práctica común en python.
  Esto signfica que, si el archivo se ejecuta directamente (sin ser importado de otro archivo) entonces la función main se ejecutará.
  __name__ es una variable especial que python asigna automáticamente a cada archivo que ejecuta.
  Si estás ejecutadno directamente desde este archivo, entonces __name__ == "__main__".
  Sino, __name__ será el nombre del archivo sin la extensión, es decir, si lo importamos desde un archivo secundario
  __name__ será "proyecto"
"""
if __name__ == "__main__":
  main()