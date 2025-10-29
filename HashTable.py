
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,capacity=10):
        self.__capacity = capacity
        self.__size = 0 #track num of items
        self.__buckets = [None] * capacity #initialize as empty linked list

    def hash(self, key):
        #use ASCII values of the char of strings to calculate the hash
        key = key.lower()
        value = sum(ord(char) for char in key)
        return hash(value) % self.__capacity

    def insert(self, key, product):
        index = self.hash(key)

        #create the start of the linked list if no collision
        if self.__buckets[index] is None:
            self.__buckets[index] = Node(key, [product])

        #travese the linked list to find the next space
        else:
            current = self.__buckets[index]

            while current:
                if current.key == key:
                    current.value.append(product)
                    return

                if current.next is None:
                    break

                current = current.next
            #insert new item into the next space
            current.next = Node(key, [product])
        #increment size of list
        self.__size += 1

    def search(self, key):
        key = key.lower()

        index = self.hash(key)

        current = self.__buckets[index]
        while current:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def delete(self, key, product_id):
        key = key.lower()
        index = self.hash(key)

        current = self.__buckets[index]
        prev = None

        while current:
            if current.key == key:
                #filter out the product with matching id
                original_length = len(current.value)
                current.value = [p for p in current.value if p.get_product_id() != product_id]

                if len(current.value) < original_length:
                    #product is deleted
                    if len(current.value) == 0:
                        #remove node if no product
                        if prev:
                            prev.next = current.next
                        else:
                            self.__buckets[index] = current.next

                        self.__size -= 1
                    return True
                return False

            prev = current
            current = current.next

        return False

    def edit(self, key, product_id, new_name, new_price, new_quantity):
        key = key.lower()
        products = self.search(key)

        if products:
            #find the product to edit
            for product in products:
                if product.get_product_id() == product_id:
                    #set the new values if not empty
                    if new_name:
                        product.set_name(new_name)
                    if new_price:
                        product.set_price(new_price)
                    if new_quantity:
                        product.set_quantity(new_quantity)

                    return True
        return False

    def get_categories(self):
        #return a list of categories in the hash table
        categories = []

        for bucket in self.__buckets:
            current = bucket

            #go through all the bucket
            while current:
                if current.key not in categories:
                    categories.append(current.key)

                current = current.next

        return sorted(categories)

    def display_all(self):
        #display all products in the hash table
        print("\n" + "="*30)
        print("ALL PRODUCTS IN INVENTORY")
        print("=" * 30)

        found_any = False

        for i, bucket in enumerate(self.__buckets):
            current = bucket

            while current:
                found_any = True

                print(f"\nCategory: {current.key.upper()}")
                print("=" * 30)

                for product in current.value:
                    product.print()
                    print("=" * 30)

                current = current.next

        if not found_any:
            print("No products found in inventory")

        print("=" * 30)