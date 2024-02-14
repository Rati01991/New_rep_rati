import time

class Cars:
    number_of_cars = 0
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        Cars.number_of_cars += 1

    def car_info(self):
        return self.__brand, self.__model, self.__year

    def age_of_car(self):
        current_year = time.localtime().tm_year
        age = current_year - self.__year
        return age

    def print_total_number_of_cars(self):
        print(f"Total number of cars: {Cars.number_of_cars}")

class ElectricCar(Cars):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.__battery_life = battery_life

    def battery_info(self):
        print(f"The battery life of this electric car is {self.__battery_life} hours")

# ==========================
st1 = Cars('Audi', 'A6', 2024)
st2 = Cars('Bmw', 'X6', 2018)

ec1 = ElectricCar('Tesla', 'S', 2023, 120)
# ec2 = ElectricCar('Nissan', 'Leaf', 2020, 205)

print(f"car info - brand, model, age: {st1.car_info()}, Age: {st1.age_of_car()}")
print(f"car info - brand, model, age: {st2.car_info()}, Age: {st2.age_of_car()}")
print(f"car info - brand, model, age: {ec1.car_info()}, Age: {ec1.age_of_car()}")
# print(f"car info - brand, model, age: {ec2.car_info()}, Age: {ec2.age_of_car()}")


ec1.battery_info()
# ec2.battery_info()

st1.print_total_number_of_cars()

#კომენტარი: დაკომენტარებული ადგილების კოდში ჩასმისას ვამატებ ელექტრო მანქანას, რის შემდეგაც მანქანების რაოდენობა
#ხდება 4 და ემატება ელექტრო მანქანის ბატარიასთან დაკავშირებული საათები.