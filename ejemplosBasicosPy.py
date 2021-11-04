

  #VARIABLES 

  numero = 26 #ENTEROS

  numero2= 6.3233 #FLOAT

  persona = 'Israel Diocares ' +" ," +"edad 26" #ESTO ES UN STRING CON CONCATENACION

  suma =  numero + numero2 #SUMA EN REALES

  multiplicacion= numero * numero2 #MULTIPLICACION EN REALES 

  division= numero /numero2 #DIVISION REALES
  
  numero3=2
  restoEntero= numero % numero3 #RESTO DE DIVISION ENTERA 
  

  #OPERADORES LOGICOS Y COMPARATIVOS

  verdad = True #BOOLEAN

  falso =False  #BOOLEAN 


  verdad and falso #CONJUNCION ; ES VERDADERA SI AMBAS PROPOSICIONES LO SON 

  verdad or falso #DISYUNCION ; ES FALSA SI AMBAS PROPOSICIONES LO SON , CUALQUIER OTRO CASO VERDAD 

  not verdad # RETORNA False ; operador negacion de una proposicion 


  numero == numero2 #RETORNA False ; OPERADOR IGUALDAD

  numero >= numero2 #RETORNA True ; OPERADOR MAYOR O IGUAL

  numero <= numero2 #RETORNA  False ; OPERADOR MENOR O IGUAL 


  #EJEMPLO CONVERSOR DE DIVISAS


  pesos  = input("¿Cuantos pesos colombianos tienes? : ")

  pesos = float(pesos)

  valorDolar = 3875


  dolares = pesos /valorDolar 

  dolares = str(dolares)

  print("tenes en dolares: "+dolares)


  ###############################CIERRA CONVERSOR DE DIVISAS

  ###TRABAJANDO CON CADENA DE CARACTERES 

  nombre = "israel"

  nombre=nombre.upper() #ISRAEL ,transforma una cadena en mayusculas

  nombre=nombre.capitalize() # #Israel . transformaa la primera letra de la cadena en mayuscula

  nombre=nombre.lower() # israel ,transforma una cadena en letras minusculas

  nombre=nombre.strip() # borra espacios basura 

  nombre = nombre.replace('a','o') # isroel remplaza una letra por la indicada 

  nombre [2] # r ,  trae un valor de la posicion indicada en la cadena 

  len(nombre) #### 6, trae la cantidad de caracteres que tiene una cadena 
  
   








