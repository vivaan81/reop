class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)

    def get_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Price:", self.price)


car1 = Car("Toyota", "Corolla", 1000000)
car1.get_info()
#i have now completed task 1 and will now commit the code once here
