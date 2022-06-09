# Juego del ahorcado
# @CristhiamDaniel
"""
Explicacion
1. Elegir aleatoriamente una palabra 
de una lista de palabras.
2. Mostrar el dibujo de una horca.
3. Mostrar un guion bajo por cada letra
de la palabra.
4. Pedir al usuario que introduzca una
letra: si no es una unica letra indicarlo. Si ya se ha dicho indicarlo.
5. COmprobar si esa letra esta contenida en la palabra elegida.
6. Si está: Volver a mostrar el dibujo de la horca como la ultima vez.
Sustituir el guión correspondiente por la letra dicha.
7. Si no está: Mostrar el dibujo de la horca al que se añade una parte.
8. Si se falla 6 veces: se completa el dibujo del ahorcado.
9. Si se aciertan todas las letras de la palabra: Ganó!
"""
import random
import os

palabras =["COLOMBIA","ECUADOR","VENEZUELA","BRASIL", "ARGENTINA", "PERU","CHILE", "BOLIVIA", "PARAGUAY", "URUGUAY","GUYANA","SURINAM"]

palabra = random.choice(palabras)

fallo0 = """
          !===N
              N
              N
              N
      =========
"""
fallo1 = """
          !===N
          O   N
              N
              N
      =========
"""
fallo2 = """
          !===N
         _O   N
              N
              N
      =========
"""
fallo3 = """
          !===N
         _O_  N
              N
              N
      =========
"""
fallo4 = """
          !===N
         _O_  N
          |   N
              N
      =========
"""
fallo5 = """
          !===N
         _O_  N
          |   N
         /    N
      =========
"""
fallo6 = """
          !===N
         _O_  N
          |   N
         / \  N
      =========
"""
letras_correctas = "" # Letras correctas dichas por el usuario
letras_todas = "" # Todas las letras dichas por el usuario
fallos = 0

while True:
  os.system("cls")
  print("************************")
  print("** JUEGO DEL AHORCADO **")
  print("************************")
  if fallos == 0:
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos == 2:
    print(fallo2)
  elif fallos == 3:
    print(fallo3)
  elif fallos == 4:
    print(fallo4)
  elif fallos == 5:
    print(fallo5)
  elif fallos == 6:
    print(fallo6)

  print()

  # Mostramos las letras acertadas y guiones bajos en las no acertadas

  resultado = ""

  for letra in palabra:
    if letra in letras_correctas:
      resultado += letra
    else:
      resultado += "_"
  print("      {}".format(resultado))
  print()
  print()


https://www.youtube.com/watch?v=9Tbw4mobaBU&list=PLh7JzoyIyU4I2Vz34FRrOfvxrR3ha49yM&index=8









      










  









    




  
  



















