def AlgoritmoNotaFinal():

  print ("---------------------------------------------------------------")
  print("Ejercicio1: Nota final del curso de Fundamentos de programación")
  print("---------------------------------------------------------------")
  #Entradas
  print("Ingrese las cuatro notas del alumno N1, N2, N3, N4 :")
  N1 = int( input("Nota de la Primera Unidad: "))
  N2 = int( input("Nota de la Segunda Unidad: "))
  N3 = int( input("Nota de la Tercera Unidad: "))
  N4 = int( input("Nota de la Trabajo Final: "))
  #Proceso
  notafinal=int((N1*0.20+N2*0.15+N3*0.15+N4*0.50))
  #Salida
  print("La Nota Final del Alumno es: ")
  print(notafinal)

def BonoDesempenoDocente():
  #definir Variables
  bonoObtenido=0.0
  #Datos de Endrada
  salarioMinimo=float(input("Ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuación que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=50:
    bonoObtenido=salarioMinimo*0.10+930
  elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
    bonoObtenido=salarioMinimo*0.40+930
  elif puntuacionObtenida>151:
    bonoObtenido=salarioMinimo*0.70+930
  #Datos de salida
  print("El docente obtendra un bono de:", bonoObtenido )

def VacunaDeTipoABYC():
  edad = int (input ('Ingresa el valor de edad: '))
  print ('Selecciona el valor de sexo.')
  print ('1.- mujer')
  print ('2.- hombre')
  print ('')
  sexo = 0
  while sexo<1 or sexo>2:
      sexo = int (input ('Seleccionó la opción: '))
      if sexo<1 or sexo>2:
          print ('Valor incorrecto. Ingresalo nuevamente.')
  if (sexo==2 and edad>=16 and edad<70) or edad<16:
      print ("A Usted le corresponde la Vacuna de Tipo: A ")
  if sexo==1 and edad>=16 and edad<70:
      print ("A Usted le corresponde la Vacuna de Tipo: B " )
  if edad>70:
      print ("A Usted le corresponde la Vacuna de Tipo: C ")
  print ()

def OperadoresMatematicos():
    a = float (input ('Ingresa el valor de a: '))
    b = float (input ('Ingresa el valor de b: '))
    print ('Selecciona el valor de operacion.')
    print ('1.- Suma')
    print ('2.- Resta')
    print ('3.- Multiplicación')
    print ('4.- División')
    print ('5.- Potencia')
    
    operacion = 0
    while operacion<1 or operacion>5:
        operacion = int (input (': '))
        if operacion<1 or operacion>5:
          ('Valor incorrecto. Ingresalo nuevamente.')
    resultado=0
    if operacion==1:
        resultado=a+b
    if operacion==2:
        resultado=a-b
    if operacion==3:
        resultado=a*b
    if operacion==4 and b!=0:
        resultado=a/b
    if operacion==5:
        resultado=a**b
    print ('Valor de resultado: ' + repr (resultado))
    print ()
    
def operacion():
  n1 = float(input("Introduce tu primer número: ") )
  n2 = float(input("Introduce tu segundo número: ") )

  opcion = 0
  while True:
      print("""
      Dime, ¿qué quieres hacer?
      
      1) Sumar los dos números
      2) Restar los dos números
      3) Multiplicar los dos números
      4) Dividir los dos números
      5) Potencia los dos números
      6) Cambiar los números elegidos
      7) Apagar calculadora
      """)
      opcion = int(input("Elige una opción: ") )     

      if opcion == 1:
          print(" ")
          print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
      elif opcion == 2:
          print(" ")
          print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
      elif opcion == 3:
          print(" ")
          print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
      elif opcion == 4:
          print(" ")
          print("RESULTADO: El cociente de",n1,"/",n2,"es igual a",n1/n2)
      elif opcion == 5:
          print(" ")
          print("RESULTADO: La potencia de",n1,"**",n2,"es igual a",n1**n2)
      elif opcion == 6:
          n1 = float(input("Introduce tu primer número: ") )
          n2 = float(input("Introduce tu segundo número: ") )
      elif opcion == 5:
          break
      else:
          print("Opción incorrecta")

def ejecutandoEjerciciosAnteriores():
  opcion = 0
  while True:
      print("""
      Dime, ¿qué ejercicio quieres volver a hacer?
      
      1) AlgoritmoNotaFinal
      2) BonoDesempenoDocente
      3) VacunaDeTipoABYC
      4) OperadoresMatematicos
      5) operacion
      6) Cambiar los números elegidos
      7) Apagar calculadora
      """)
      opcion = int(input("Elige una opción: ") )
      if opcion == 1:
          print ("---------------------------------------------------------------")
          print("Ejercicio1: Nota final del curso de Fundamentos de programación")
          print("---------------------------------------------------------------")
          #Entradas
          print("Ingrese las cuatro notas del alumno N1, N2, N3, N4 :")
          N1 = int( input("Nota de la Primera Unidad: "))
          N2 = int( input("Nota de la Segunda Unidad: "))
          N3 = int( input("Nota de la Tercera Unidad: "))
          N4 = int( input("Nota de la Trabajo Final: "))
          #Proceso
          notafinal=int((N1*0.20+N2*0.15+N3*0.15+N4*0.50))
          #Salida
          print("La Nota Final del Alumno es: ")
          print(notafinal)

#EJERCICIOS DE EXAMEN UNIDAD 1 E.M.A.Y

def AlgoritmoNotaFinalEMAY():

  print ("---------------------------------------------------------------")
  print("Ej. 01: NOTA FINAL DEL CURSO DE FUNDAMENTOS DE PROGRAMACIÓN")
  print("---------------------------------------------------------------")
  #Entradas
  print("Ingrese las cuatro notas del alumno N1, N2, N3, N4 :")
  N1 = int( input("Nota de la Primera Unidad: "))
  N2 = int( input("Nota de la Segunda Unidad: "))
  N3 = int( input("Nota de la Tercera Unidad: "))
  N4 = int( input("Nota de la Trabajo Final: "))
  #Proceso
  notafinal=int((N1*0.20+N2*0.15+N3*0.15+N4*0.50))
  #Salida
  print ("---------------------------------------------------------------")
  print("La Nota Final del Alumno es:" ,notafinal)
  print("---------------------------------------------------------------")

def BonoDesempenoDocenteEMAY():
  #definir Variables
  bonoObtenido=0.0
  print ("---------------------------------------------------------------")
  print("Ej. 02: BONO POR DESEMPEÑO DEL DOCENTE")
  print("---------------------------------------------------------------")
  #Datos de Endrada
  salarioMinimo=float(input("Ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuación que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=50:
    bonoObtenido=salarioMinimo*0.10+930
  elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
    bonoObtenido=salarioMinimo*0.40+930
  elif puntuacionObtenida>151:
    bonoObtenido=salarioMinimo*0.70+930
  #Datos de salida
  print ("---------------------------------------------------------------")
  print("El docente obtendra un bono de:", bonoObtenido )
  print ("---------------------------------------------------------------")

def VacunasContraelCOVID19EMAY():
  print ("---------------------------------------------------------------")
  print("Ej. 03: VACUNAS DE TIPOS A,B y C CONTRA EL COVID19")
  print("---------------------------------------------------------------")
  edad = int (input ('Ingresa el valor de edad: '))
  print ('Selecciona el valor de sexo.')
  print ('1.- mujer')
  print ('2.- hombre')
  print ('')
  sexo = 0
  while sexo<1 or sexo>2:
      sexo = int (input ('Seleccionó la opción: '))
      if sexo<1 or sexo>2:
        print ("---------------------------------------------------------------")
        print ('Valor incorrecto. Ingresalo nuevamente.')
        print ("---------------------------------------------------------------")
  if (sexo==2 and edad>=16 and edad<70) or edad<16:
      print ("---------------------------------------------------------------")
      print ("A Usted le corresponde la Vacuna de Tipo: A ")
      print ("---------------------------------------------------------------")
  if sexo==1 and edad>=16 and edad<70:
      print ("---------------------------------------------------------------")
      print ("A Usted le corresponde la Vacuna de Tipo: B " )
      print ("---------------------------------------------------------------")
  if edad>70:
      print ("---------------------------------------------------------------")
      print ("A Usted le corresponde la Vacuna de Tipo: C ")
      print ("---------------------------------------------------------------")
  print ()

def OperacionesMatematicasEMAY():
  print ("---------------------------------------------------------------")
  print("Ej. 04: OPERACIONES ARITMÉTICAS")
  print("---------------------------------------------------------------")
  n1 = float(input("Introduce tu primer número: ") )
  n2 = float(input("Introduce tu segundo número: ") )

  opcion = 0
  while True:
      print("""
      Dime, ¿qué quieres hacer?
      
      1) Sumar
      2) Restar
      3) Multiplicar
      4) Dividir
      5) Potencia
      6) Cambiar los números elegidos
      7) Apagar Algoritmo.
      """)
      opcion = int(input("Elige una opción: ") )     

      if opcion == 1:
          print(" ")
          print ("---------------------------------------------------------------")
          print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
          print ("---------------------------------------------------------------")
      elif opcion == 2:
          print(" ")
          print ("---------------------------------------------------------------")
          print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
          print ("---------------------------------------------------------------")
      elif opcion == 3:
          print(" ")
          print ("---------------------------------------------------------------")
          print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
          print ("---------------------------------------------------------------")
      elif opcion == 4:
          print(" ")
          print ("---------------------------------------------------------------")
          print("RESULTADO: El cociente de",n1,"/",n2,"es igual a",n1/n2)
          print ("---------------------------------------------------------------")
      elif opcion == 5:
          print(" ")
          print ("---------------------------------------------------------------")
          print("RESULTADO: La potencia de",n1,"**",n2,"es igual a",n1**n2)
          print ("---------------------------------------------------------------")
      elif opcion == 6:
          n1 = float(input("Introduce tu primer número: ") )
          n2 = float(input("Introduce tu segundo número: ") )
      elif opcion == 7:
          break
      else:
          print ("---------------------------------------------------------------")
          print("Opción incorrecta")
          print ("---------------------------------------------------------------")

def EjecutandoEjerciciosAnterioresEMAY():
  opcion = 0
  while True:
      print("""
      Dime, ¿qué ejercicio quieres volver a hacer?
      
      1) AlgoritmoNotaFinalEMAY
      2) BonoDesempenoDocenteEMAY
      3) VacunasContraelCOVID19EMAY
      4) OperacionesMatematicasEMAY
      5) TerminarAlgoritmo
      """)
      opcion = int(input("Elige una opción: ") )
      if opcion == 1:
          print ("---------------------------------------------------------------")
          print("Ej. 01: NOTA FINAL DEL CURSO DE FUNDAMENTOS DE PROGRAMACIÓN")
          print("---------------------------------------------------------------")
          #Entradas
          print("Ingrese las cuatro notas del alumno N1, N2,N3, N4 :")
          N1 = int( input("Nota de la Primera Unidad: "))
          N2 = int( input("Nota de la Segunda Unidad: "))
          N3 = int( input("Nota de la Tercera Unidad: "))
          N4 = int( input("Nota de la Trabajo Final: "))
          #Proceso
          notafinal=int((N1*0.20+N2*0.15+N3*0.15+N4*0.50))
          #Salida
          print ("---------------------------------------------------------------")
          print("La Nota Final del Alumno es:" ,notafinal)
          print("---------------------------------------------------------------")
      elif opcion == 2:
          print(" ")
          #definir Variables
          bonoObtenido=0.0
          print ("---------------------------------------------------------------")
          print("Ej. 02: BONO POR DESEMPEÑO DEL DOCENTE")
          print("---------------------------------------------------------------")
          #Datos de Endrada
          salarioMinimo=float(input("Ingrese el salario minimo:"))
          puntuacionObtenida=float(input("Ingrese la puntuación que ha obtenido:"))
          #Proceso
          if puntuacionObtenida<=100 and puntuacionObtenida>=50:
            bonoObtenido=salarioMinimo*0.10+930
          elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
            bonoObtenido=salarioMinimo*0.40+930
          elif puntuacionObtenida>151:
            bonoObtenido=salarioMinimo*0.70+930
          #Datos de salida
          print ("---------------------------------------------------------------")
          print("El docente obtendra un bono de:", bonoObtenido )
          print ("---------------------------------------------------------------")
      elif opcion == 3:
          print(" ")
          print ("---------------------------------------------------------------")
          print("Ej. 03: VACUNAS DE TIPOS A,B y C CONTRA EL COVID19")
          print("---------------------------------------------------------------")
          edad = int (input ('Ingresa el valor de edad: '))
          print ('Selecciona el valor de sexo.')
          print ('1.- mujer')
          print ('2.- hombre')
          print ('')
          sexo = 0
          while sexo<1 or sexo>2:
              sexo = int (input ('Seleccionó la opción: '))
              if sexo<1 or sexo>2:
                print ("---------------------------------------------------------------")
                print ('Valor incorrecto. Ingresalo nuevamente.')
                print ("---------------------------------------------------------------")
          if (sexo==2 and edad>=16 and edad<70) or edad<16:
              print ("---------------------------------------------------------------")
              print ("A Usted le corresponde la Vacuna de Tipo: A ")
              print ("---------------------------------------------------------------")
          if sexo==1 and edad>=16 and edad<70:
              print ("---------------------------------------------------------------")
              print ("A Usted le corresponde la Vacuna de Tipo: B " )
              print ("---------------------------------------------------------------")
          if edad>70:
              print ("---------------------------------------------------------------")
              print ("A Usted le corresponde la Vacuna de Tipo: C ")
              print ("---------------------------------------------------------------")
          print ()
      elif opcion == 4:
          print(" ")
          print ("---------------------------------------------------------------")
          print("Ej. 04: OPERACIONES ARITMÉTICAS")
          print("---------------------------------------------------------------")
          n1 = float(input("Introduce tu primer número: ") )
          n2 = float(input("Introduce tu segundo número: ") )

          opcion = 0
          while True:
              print("""
              Dime, ¿qué quieres hacer?
              
              1) Sumar
              2) Restar
              3) Multiplicar
              4) Dividir
              5) Potencia
              6) Cambiar los números elegidos
              7) Apagar Algoritmo.
              """)
              opcion = int(input("Elige una opción: ") )     

              if opcion == 1:
                  print(" ")
                  print ("---------------------------------------------------------------")
                  print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
                  print ("---------------------------------------------------------------")
              elif opcion == 2:
                  print(" ")
                  print ("---------------------------------------------------------------")
                  print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
                  print ("---------------------------------------------------------------")
              elif opcion == 3:
                  print(" ")
                  print ("---------------------------------------------------------------")
                  print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
                  print ("---------------------------------------------------------------")
              elif opcion == 4:
                  print(" ")
                  print ("---------------------------------------------------------------")
                  print("RESULTADO: El cociente de",n1,"/",n2,"es igual a",n1/n2)
                  print ("---------------------------------------------------------------")
              elif opcion == 5:
                  print(" ")
                  print ("---------------------------------------------------------------")
                  print("RESULTADO: La potencia de",n1,"**",n2,"es igual a",n1**n2)
                  print ("---------------------------------------------------------------")
              elif opcion == 6:
                  n1 = float(input("Introduce tu primer número: ") )
                  n2 = float(input("Introduce tu segundo número: ") )
              elif opcion == 7:
                  break
              else:
                  print ("---------------------------------------------------------------")
                  print("Opción incorrecta")
                  print ("---------------------------------------------------------------")
      elif opcion == 5:
          break
      else:
          print ("---------------------------------------------------------------")
          print("Opción incorrecta")
          print ("---------------------------------------------------------------")

#AlgoritmoNotaFinal()
#BonoDesempenoDocente()
#VacunaDeTipoABYC()
#OperadoresMatematicos()
#operacion()
#ejecutandoEjerciciosAnteriores()
#AlgoritmoNotaFinalEMAY()
#BonoDesempenoDocenteEMAY()
#VacunasContraelCOVID19EMAY()
#OperacionesMatematicasEMAY()
EjecutandoEjerciciosAnterioresEMAY()
