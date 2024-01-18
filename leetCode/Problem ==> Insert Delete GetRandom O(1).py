class RandomizedSet:

    def __init__(self):
        self.randomizedSet = []

    def insert(self, val: int) -> bool:
        if val not in self.randomizedSet:
            self.randomizedSet.append(val)
            return True
        else: False

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            self.randomizedSet.remove(val)
            return True
        else: False

    def getRandom(self) -> int:
        import random
        return random.choice(self.randomizedSet)

#IMPROVED VERSION
"""
The approach is to use a Python list (self.list) to store the elements and a Python dictionary (self.dict) to store the index of each element in the list.

For the insert operation, we add the element to the end of the list and record its index in the dictionary.
For the remove operation, we first find the index of the element to remove in the list using the dictionary. Then we swap this element with the last element in the list, update the index of the last element in the dictionary, and finally pop the last element off the list and remove the element from the dictionary.
For the getRandom operation, we simply use Python's built-in random.choice function to get a random element from the list.
"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # Move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # Remove last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
