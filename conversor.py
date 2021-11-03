"""pesos  = input("¿Cuantos pesos ARGENTINOS tienes? : ")

pesos = float(pesos)

valorDolar = 197.5

dolares = pesos /valorDolar
dolares =round(dolares,2)
dolares = str(dolares)
print("tenes en dolares: "+dolares)

#FUNCION DOLARES A PESOS ARGENTINOS

dolar =input("¿Cuantos dolares tenes?")

dolar = float (dolar)

ars =dolar * valorDolar

ars = round(ars,2)

ars = str(ars)

print ("Tenes en pesos argentinos : "+ars)

"""


###MULTLIPES DIVISAS

menu = """

WELCOME TO FOREIGN EXCHANGE CONVERTER

Please enter one option in number

1 - Argentine money
2 - Colombian money
3 - Brasil money

Choice an option: """

option = int (input(menu))

if option ==1:
    pesos  = input("¿How many argentine money you have? : ")
    pesos = float(pesos)
    valorDolar = 197.5
    dolares = pesos /valorDolar
    dolares =round(dolares,2)
    dolares = str(dolares)
    print("you have in doalrs : "+dolares)
elif option==2:
    pesos  = input("¿How many Colombian money you have? : ")
    pesos = float(pesos)
    valorDolar = 3833.67
    dolares = pesos /valorDolar
    dolares =round(dolares,2)
    dolares = str(dolares)
    print("you have in doalrs : "+dolares)
elif option ==3:
    pesos  = input("¿How many Brazilian real you have? : ")
    pesos = float(pesos)
    valorDolar = 5.67
    dolares = pesos /valorDolar
    dolares =round(dolares,2)
    dolares = str(dolares)
    print("you have in doalrs : "+dolares)
else:
    print("Please enter one option correct")
