def conversor(tipo_pesos,valor_dolar):
    pesos=int(input("cuantos pesos" +tipo_pesos+" tienes?: "))
    valor_dolar=valor_dolar
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
    return pesos



menu = """
Bienvenido al conversor de monedas ❤️

1- pesos cop
2- pesos ar
3- pesos mx

elige una opcion: """
opcion = int(input(menu))
if opcion ==1:
    conversor("colombianos", 5000)
if opcion ==2:
    conversor("argentinos", 64)
if opcion ==3:
    conversor("mexicanos", 24)
