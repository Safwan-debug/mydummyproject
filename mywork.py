print('Bismilla')

def saf():
    n = 10
    return n

print(saf())

class Mywork:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
        
    def b_print_(self):
        print('My name is :',self.name)
        print('my age is :',self.age)
        print('my braanch is :',self.branch)
        
    

obj = Mywork("safwan",25,"BE")
obj.b_print_()
        