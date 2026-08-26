
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("The vehicle has started.")

    def stop(self):
        print("The vehicle has stopped.")

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)



class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def drive(self):
        print("The car is being driven.")

    
    def display_info(self):
        super().display_info()
        print("Number of doors:", self.number_of_doors)



class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def ride(self):
        print("The motorcycle is being ridden.")

    # Method overriding
    def display_info(self):
        super().display_info()
        print("Engine CC:", self.engine_cc)



car1 = Car("Toyota", "Corolla", 2022, 4)


car1.start()
car1.drive()
car1.display_info()
car1.stop()

print("--------------------")



motorcycle1 = Motorcycle("Honda", "CBR", 2023, 600)


motorcycle1.start()
motorcycle1.ride()
motorcycle1.display_info()
motorcycle1.stop()