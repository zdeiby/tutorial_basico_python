def palindromo(palabra):
    palabra=palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra=input('escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")

if __name__ == '__main__':
    run()
