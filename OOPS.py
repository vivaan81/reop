class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.__price = price

    def apply_discount(self, discount):
        self.__price = self.__price - (self.__price * discount / 100)

    def get_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Price:", self.__price)

    def get_price(self):
    return self.__price

    def set_price(self, price):
    self.__price = price
    
class ElectricCar(Car):
    def __init__(self, make, model, price, battery_range):
        super().__init__(make, model, price)
        self.battery_range = battery_range

    def get_info(self):
        super().get_info()
        print("Battery Range:", self.battery_range)

class SportsCar(Car):
    def __init__(self, make, model, price, top_speed):
        super().__init__(make, model, price)
        self.top_speed = top_speed

    def get_info(self):
        super().get_info()
        print("Top Speed:", self.top_speed)


car1 = Car("Toyota", "Corolla", 1000000)
car1.get_info()
