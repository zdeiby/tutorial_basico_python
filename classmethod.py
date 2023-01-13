class Operation:
    def __init__(self):
        self
    @classmethod
    def resta(cls,num1,num2):
        print(num1-num2)

print(Operation.resta(6,3))