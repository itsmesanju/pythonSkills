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
        
