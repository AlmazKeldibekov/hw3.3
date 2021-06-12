class Pizza:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
    
    @classmethod
    def margarita(cls):
        p = Pizza('margarita',['mozarella', 'tomatos', 'olives']) 
        return p
    
    @staticmethod
    def calculate_area(radius):
        area = 3.14 * radius**2
        return f'Площадь пиццы равна: {area}'

marg = Pizza.margarita()
print(marg.name)
print(marg.ingredients)
print(marg.calculate_area(30))




