class car:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year



    def get_model(self) :
        return self.model

    def get_make(self) :
        return self.make

    def get_year(self):
        return self.year



car1 = car("demio","nissan",2018)
car2 = car("hilux","toyota",2020) 
car3 = car("x6","bmw",2009) 

car3.set_year(2023)
car1.set_year(2026)

def set_model(self,model):
    self.model = model

def set_make(self,make):
    self.make = make

def set_year(self,year):
    self.year = year

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())


print(car1.get_year())
print(car3.get_year())



