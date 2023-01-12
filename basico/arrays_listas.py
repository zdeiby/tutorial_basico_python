def run():
    lista = [1,2,3,4,5]
    for li in lista:
        print(li)
    lista2 = [6,7,8,9]
    lista3=lista+lista2
    print(lista3)
    lista * 5 # se repite 5 veces la cadena

if __name__ == '__main__':
    run()