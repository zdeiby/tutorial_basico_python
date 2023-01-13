class Book():
    def __init__(self, title, author, electronic):
        self.title= title
        self.author=author
        self.electronic=electronic
    def __del__(self):
        print("acabas de llamar al metodo destructor. se murio :c")
  

#book1=Book("el señor","cohelo",False)
#book2=Book("el señor caiman","cohelo",False)
#book3=Book("el señor de los cielos","cohelo",False)
#book4=Book("el señor de los anillos","cohelo",False)

#print(book3.__dict__)
#del book1 
#print(book1)

#ejercicio 2

class RationalNumber():
    def __init__(self, n,d=1):
        if type(n) is int and type(d) is int:
            self.numerator=n
            self.denominator=d
        else:
            print("el numerador y el denominador debe ser enteros")

ec1=RationalNumber(1,2)

#ejercicio 3

class Rectangle():
    def __init__(self, base = 1 , height=1, color="blue"):
        self.base=base
        self.height=height
        self.color= color
    def perimeter(self):
        return 2*self.base + 2 * self.height
    def area(self):
        return self.base*self.height

rect1= Rectangle(5,2,"red")
print("el perimetro es {}".format(rect1.perimeter()))