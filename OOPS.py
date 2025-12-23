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
    


car1 = Car("Toyota", "Corolla", 1000000)
car1.get_info()
