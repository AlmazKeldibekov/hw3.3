class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        return(f'My name is {self.name}')


def get_name(*args):
    for i in args:
        try:
            print(i.show_name())
        except:
            print("У данного аргумента нет имени")


Iliyas = Person('Iliyas')
Kairat = Person('Kairat')
Zhamshid = Person('Zhamshid')
get_name(Iliyas,Kairat,Zhamshid)
