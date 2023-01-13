class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca= marca
        self.color= color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros= cilindros
        self.tipo= tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

dicionario = {
    "numero":1,
    "numero2":2,
    "numero3":3
    }

dias=["lunes", "martes","miercoles"]
numeros=[1,2,3]
cadena=dicionario.items()
#print(cadena)

dici={dias:numeros for dias,numeros in zip(dias,numeros)}
#print(dici)

#print(dicionario)
lista={} 
for leer in dicionario:
    #print(leer[1])
    #print(leer[0],len(dicionario)-1)
    lista=dicionario

print(lista.items(0))

