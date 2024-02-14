class Car:
    def __new__(cls, *args, **kwargs):
        print("Now I want to create instance using method __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        print("Now I want to create instance using method __init__")
        self._brand = brand
        self._model = model
        self._year = year

    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Sting is needed")

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if isinstance(model, str):
            self._model = model
        else:
            print("Sting is needed")

    def get_model(self):
        return self._model

    def set_year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            print("Integer is needed")

    def get_year(self):
        return self._year

# ==================================
my_car = Car("Mercedes", "Cla", 2020)

print("Brand:", my_car.get_brand())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# test
my_car.set_brand(1)  
my_car.set_model(2)  
my_car.set_year("3")