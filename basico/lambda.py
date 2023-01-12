tupla= lambda x: (x,2*x,x**2)
tupla(3)
print(tupla(4))

num = [-5,-3,5,2,1,3,-2,-9,0.4,-0.01]
positivos=list(filter(lambda x: x>0, num))
print(positivos)