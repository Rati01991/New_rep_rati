# #1 დავალება SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია
# #ვარიანტი 1
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def get_discounted_price(self, discount):
#         discounted_price = self.price * (1 - discount)
#         return discounted_price

# # =========================
# book = Book("100 Years of Solitude", "Gabriel Garcia Marquez", 20)  # Create a Book.
# discounted_price = book.get_discounted_price(0.1)  # 10% discount.
# print("Title:", book.title)
# print("Author:", book.author)
# print("Discounted price:", discounted_price)


#2 დავალება დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment. Open/Closed Principle
# class Payment:
#     def process_payment(self, amount):
#         pass

# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Processing credit card payment of ${amount}")

# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         print(f"Processing PayPal payment of ${amount}")

# # =======================================
# credit_card_payment = CreditCardPayment()
# credit_card_payment.process_payment(70)
# paypal_payment = PayPalPayment()
# paypal_payment.process_payment(80)

# #3 დავალება: გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# class Vehicle:
#     def fuel_capacity(self):
#         return "100 liters"

# class ElectricCar(Vehicle):
#     def fuel_capacity(self):
#         return "100 liters (equivalent battery capacity is 100 kWh)"

# # =================================================
# vehicle = Vehicle()
# print("Vehicle fuel capacity:", vehicle.fuel_capacity())

# electric_car = ElectricCar()
# print("Electric car fuel capacity:", electric_car.fuel_capacity())


#4 შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
#ვარიანტი 1
# class AudioPlayer:
#     def play_audio(self):
#         pass

# class VideoPlayer:
#     def play_video(self):
#         pass

#ვარიანტი 2
# from abc import ABC, abstractmethod

# class Player(ABC):
#     @abstractmethod
#     def play(self):
#         pass

# class AudioPlayer(Player):
#     def play(self):
#         return "Playing audio"

# class VideoPlayer(Player):
#     def play(self):
#         return "Playing video"
    
# # =================================
# audio_player = AudioPlayer()
# print(audio_player.play())  

# video_player = VideoPlayer()
# print(video_player.play())  


#5 შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# from abc import ABC, abstractmethod

# class Display(ABC):
#     @abstractmethod
#     def show(self, data):
#         pass

# class ConsoleDisplay(Display):
#     def show(self, data):
#         print(data)

# class WeatherStation:
#     def __init__(self, display):
#         self.display = display

#     def report(self):
#         self.display.show("Weather Data")

# # ===========================================
# console_display = ConsoleDisplay()
# weather_station = WeatherStation(console_display)
# weather_station.report()