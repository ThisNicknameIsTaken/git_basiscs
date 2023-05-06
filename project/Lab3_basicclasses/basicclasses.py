class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price})"

class Book(Item):
    def __init__(self, name: str, price: float, author: str):
        super().__init__(name, price)
        self.author = author
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.author})"

class Food(Item):
    def __init__(self, name: str, price: float, expiry_date: str):
        super().__init__(name, price)
        self.expiry_date = expiry_date
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.expiry_date})"

class Toy(Item):
    def __init__(self, name: str, price: float, age_range: str):
        super().__init__(name, price)
        self.age_range = age_range
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.age_range})"
