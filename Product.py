
class BabyProduct:

    def __init__(self,pid,name,category,price,quantity):
        self.__productId = pid
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity

    #getter
    def get_product_id(self):
        return self.__productId

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    #setter
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def print(self):
        print(f'Product Id: {self.__productId}')
        print(f'Product Name: {self.__name}')
        print(f'Product Price: ${self.__price:.2f}')
        print(f'Product Category: {self.__category}')
        print(f'Product Quantity: {self.__quantity}')