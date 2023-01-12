class Animales:
    def __init__(self,animal, nombre,raza="callejero"):
        self.animal=animal
        self.nombre=nombre
        self.raza=raza
        return print(self.animal,self.nombre, self.raza)

       
perro=Animales("perro","lucas")
gato=Animales("vaca","lola")
loro=Animales("loro","cacao")
gallina=Animales("gallina","doña gallina")


#para saber si una funcion es instancia colocamos 
print(isinstance(perro,Animales)) #si devuelve true es, si devuelva false, no 

