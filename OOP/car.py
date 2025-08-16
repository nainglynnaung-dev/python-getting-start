class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
            print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
#
# car=Car("Ford","Mustang",2019)
# car1=Car("Ford","Mustang",2019)

# car1.display_info()
# car.display_info()

class ElectricCar(Car):

    def __init__(self, make, model, year, battery_capacity):
        super().__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}(Electric Car)")



        ecar=ElectricCar("Toyota","Mustang",2019,"200 Wh")
        ecar.display_info()