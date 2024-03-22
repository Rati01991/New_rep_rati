import unittest #ვაკეთებ unittest-ის იმპორტს.
from vehicle import Vehicle #ვაკეთებ Vehicle კლასის იმპორტს vehicle.py ფაილიდან.
from vehicle import ElectricVehicle #დავაიმპორტირე ElectricVehicle კლასიც. 

class TestVehicle(unittest.TestCase): #ვქმნი TestVehicle კლასს, რომელიც მემკვიდრეობით იღებს unittest.TestCase-ს.
    def setUp(self): #SetUp მეთოდში ვქმნი Vehicle კლასის მაგალითს ტესტირებისთვის.
        self.vehicle = Vehicle("Maserati", "Granturismo", 2024)
#სატესტო მეთოდები: initialization, fuel_up და test_drive.
    def test_initialization(self): #test_initialization აკეთებს ავტომობილის ინიციალიზაციის ტესტირებას.
        self.assertEqual(self.vehicle.brand, "Maserati") #ბრენდის სწორად მინიჭება, ატრიბუტი სტრიქონის ტოლია.
        #self.assertEqual(self.vehicle.brand, "1") #->AssertionError: 'Maserati' != '1' (მაგალითი)
        self.assertEqual(self.vehicle.model, "Granturismo") #მოდელის სწორად მინიჭება.
        self.assertEqual(self.vehicle.year, 2024) #წლის სწორად მინიჭება, ატრიბუტი მთელი რიცხვის ტოლია.
        self.assertEqual(self.vehicle.gaz_tank_size, 45) #არის თუ არა გაზის ავზის მოცულობა 45-ს.
        #self.assertEqual(self.vehicle.gaz_tank_size, #-> 46) AssertionError: 45 != 46 (მაგალითი)
        self.assertEqual(self.vehicle.fuel_level, 0) #არის თუ არა ბენზინის ავზის მოცულობა 45-ს.
#შევამოწმე თითოეული ატრიბუტის სისწორე, თუ ეს ტესტი ვერ გაიარა სახეზე იქნება პრობლემა ლოგიკაში Vehicle კლასში.
        
    def test_fuel_up(self): #->ავზის გავსების შემოწმება.
        self.vehicle.fuel_up
        self.assertEqual(self.vehicle.fuel_level, self.vehicle.gaz_tank_size) #ვამოწმებ მათ ტოლობას - 45.
        self.assertIn("Gas tank is now full", self.vehicle.fuel_up) #fuel_up მეთოდი დააბრუნებს შეტყობინებას, 
        #რომელიც მიუთითებს, რომ გაზის ავზი ახლა სავსეა. ის უზრუნველყოფს, რომ fuel_up-ის გამოძახების შემდეგ,
        #ავტომობილის საწვავის დონე სწორად განახლდება ბენზინის ავზის ზომამდე და მეთოდი აბრუნებს შეტყობინებას,
        #რომელიც მიუთითებს, რომ გაზის ავზი ახლა სავსეა. თუ ეს ვერ დამტკიცდა, ეს მიუთითებს პრობლემაზე fuel_up 
        #მეთოდის განხორციელებასთან დაკავშირებით.


    def test_drive(self):
        self.assertIn("Granturismo is now driving", self.vehicle.drive) #self.vehicle.drive იძახებს drive
        #მეთოდს, რომელმაც უნდა დააბრუნოს სტრიქონი, რომელიც მიუთითებს, რომ მანქანა ახლა მოძრაობს.
        #self.assertIn "Granturismo is now driving".

class TestElectricVehicle(unittest.TestCase):
    def setUp(self):
        self.electric_vehicle = ElectricVehicle("Kia", "EV9", 2024)

    def test_initialization(self):
        self.assertEqual(self.electric_vehicle.brand, "Kia")
        self.assertEqual(self.electric_vehicle.model, "EV9")
        self.assertEqual(self.electric_vehicle.year, 2024)
        self.assertEqual(self.electric_vehicle.battery_size, 85)
        self.assertEqual(self.electric_vehicle.charge_level, 0)

    def test_charge(self):
        self.electric_vehicle.charge
        self.assertEqual(self.electric_vehicle.charge_level, 100)
        self.assertIn("The vehicle is now charged", self.electric_vehicle.charge)

    def test_fuel_up(self):
        self.assertEqual(self.electric_vehicle.fuel_up, "This vehicle has no fuel tank!")

if __name__ == "__main__": #მიმდინარეობს თუ არა სკრიპტი, როგორც მთავარი პროგრამა.
    unittest.main() #ვიყენებ ტესტირების გასაშვებად.