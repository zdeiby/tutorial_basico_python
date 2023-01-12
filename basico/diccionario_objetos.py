def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    #print(mi_diccionario['llave1'])
    #print(mi_diccionario['llave2'])
   # print(mi_diccionario['llave3'])
    poblacion_paises= {
        'argentina': 446654656,
        'brazil': 20120000,
        'colombia':1231231283,
    }
   # print(poblacion_paises['argentina'])

    for paises, poblacion in poblacion_paises.items():
        print(paises, poblacion)

if __name__ == '__main__':
    run()