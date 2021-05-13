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
    
    operacion = 0
    while operacion<1 or operacion>4:
        operacion = int (input (': '))
        if operacion<1 or operacion>4:
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
    print ('Valor de resultado: ' + repr (resultado))
    print ()
    
AlgoritmoNotaFinal()
#BonoDesempenoDocente()
#VacunaDeTipoABYC()
#OperadoresMatematicos()