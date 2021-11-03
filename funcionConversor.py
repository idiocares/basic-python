def conversorDivisas(tipoMoneda,valor_dolar):
    pesos = float (input ("cuantos pesos "+tipoMoneda+" Tenes? "))
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    return dolares

##PROGAMA PRINCIPAL


menu = """

WELCOME TO FOREIGN EXCHANGE CONVERTER

Please enter one option in number

1 - Argentine money
2 - Colombian money
3 - Brasil money

Choice an option: """

option = int (input(menu))

if option ==1:
    dolares = conversorDivisas("argentino",199)
    dolares = str(dolares)
    print ("you have in doalrs: "+dolares)
elif option==2:
    dolares=conversorDivisas("colombiano",3883.67)
    dolares = str(dolares)
    print("you have in doalrs : "+dolares)
elif option ==3:
    dolares = conversorDivisas("real brasilero",5.667)
    dolares = str(dolares)
    print("you have in doalrs : "+dolares)
else:
    print("Please enter one option correct")



