from platform import processor


class BabyProduct:

    def __init__(self,pid,name,category,price,quantity):
        self.__productId = pid
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity

    def print(self):
        print(f'Product Id: {self.__productId}')
        print(f'Product Name: {self.__name}')
        print(f'Product Price: ${self.__price}')
        print(f'Product Category: {self.__category:.2f}')
        print(f'Product Quantity: {self.__quantity}')