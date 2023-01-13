

class Circulo:
    @staticmethod
    def pi():
        return 3.1416
   

    def __init__(self, radio):
        self.radio=radio
    def area(self): #metodos de instancias
        return self.radio*self.radio * Circulo.pi()
     

print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())
