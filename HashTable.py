class Node:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__next = None


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

    def delete(self):
        return None

    def edit(self):
        return None
