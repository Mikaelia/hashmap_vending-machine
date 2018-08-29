#!/usr/bin/env python3
"""
Module contains hash map and vending machine functionality
"""
import sys
import cmd
import shlex

class VendingHash():
    """
    Vending machine implementing hash map
    """
    def __init__(self, size):
        """
        Initializes VendingHash class

        Attributes:
            buckets[list]: The hash map containing (size) buckets
            size[int]: Number of buckets in hash map
        """
        #initialize empty hash map
        self.buckets = [None] * size
        self.size = size


    def get_hash(self, key):
        """
        The hash function. Returns the hashed key_value that indicates bucket
        in which to place item
        """
        total = 0
        # adds ascii value of key string, modulo by size to produce hash
        for c in str(key):
            total += ord(c)
        return total % self.size


    def add(self, key, values={}):
        """
        Add item to the machine
        """
        hash_key = self.get_hash(key)
        item = [key, values]

        # If hash bucket is empty
        if self.buckets[hash_key] is None:
            self.buckets[hash_key] = [item]
        else:
            # Traverse through pairs stored in hash bucket
            for pair in self.buckets[hash_key]:
                if pair[0] == key:
                    # Search item dict for price input, and update item price if not None
                    price = values.get('price')
                    if price is not 0:
                        pair[1]['price'] = values.get('price')
                    # Update number of items
                    total_count = pair[1].get('count') + values.get('count')
                    pair[1]['count'] = total_count
                    return True
            # Item not in hash table. Append to bucket
            self.buckets[hash_key].append(item)
            return True


    def buy(self, key):
        """
        Removes value
        """
        hash_key = self.get_hash(key)
        bucket = self.buckets[hash_key]

        if bucket:
            for i in range(0, len(bucket)):
                print(bucket[i][0])
                if bucket[i][0] == key:
                    print("You bought a {} for ${:.2f}".format(bucket[i][0], bucket[i][1].get("price")))
                    bucket[i][1].update({"count": bucket[i][1].get("count") - 1})


    def tell(self):
        """
        Describes items in hash
        """
        flag = None
        for val in self.buckets:
            if val:
                flag = 1
                for i in range(len(val)):
                    count = val[i][1].get("count", "Out of Stock")
                    item = val[i][0]
                    price = val[i][1].get("price")
                    if not price:
                        price = 0

                    if val[i][1].get("count") > 1:
                        print("There are {0} {1}s left. {1}s cost ${2:.2f}".format(count, item.title(), price))
                    else:
                        print("There is {0} {1} left. {1}s cost ${2:.2f}".format(count, item.title(), price))
        
        if not flag:
            print("There is nothing in the machine")

    def find(self, key):
        """
        Describes individual item
        """
        hash_key = self.get_hash(key)
        bucket = self.buckets[hash_key]

        if bucket:
            for i in range(0, len(bucket)):
                if bucket[i][0] == key:
                    print("{}s cost ${:.2f}.".format(bucket[i][0], bucket[i][1].get("price")))
                    return True
        else:
            return False

    def value(self):
        """
        Describes items in hash
        """
        food_value = 0
        for val in self.buckets:
            if val:
                for i in range(len(val)):
                    food_value += val[i][1].get("price") * val[i][1].get("count")
        print("This machine has ${:.2f} worth of food".format(food_value))


    def restock(self):
        self.add("Apple", {"count": 10, "price": 1.00})
        self.add("Cheese", {"count": 10, "price": 1.50})
        self.add("Chocolate", {"count": 10, "price": 2.00})
        self.add("Cracker", {"count": 10, "price": 1.69})
        self.add("Cookie", {"count": 10, "price": 3.00})
        self.add("Carrot", {"count": 10, "price": 2.00})
        self.add("Gatorade", {"count": 10, "price": 2.75})
        self.add("Yogurt", {"count": 10, "price": 2.20})


    def schema(self):
        for val in self.buckets:
            print(val)

if __name__ == '__main__':
    snackatron = VendingHash(5)