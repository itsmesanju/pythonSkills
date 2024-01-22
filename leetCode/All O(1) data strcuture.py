"""init: Create two dictionaries. self.keys will store keys grouped by their counts, and 
self.count will store the count of each key.

inc(): Increase the count of a given key in self.count. Update self.keys by removing the 
key from its previous count group and adding it to the new count group.

dec(): Decrease the count of a given key in self.count. Update self.keys similarly to the increment method.

getMaxKey() and getMinKey(): Retrieve the keys with maximum and minimum counts by accessing 
the corresponding entries in self.keys
"""

class AllOne:

    def __init__(self):
        self.keys = {}
        self.count = {}

    def inc(self, key: str) -> None:
        if key in self.count:
            self.count[key] = self.count[key] + 1
        else:
            self.count[key] = 1

        c = self.count[key]

        if c - 1 in self.keys:
            self.keys[c - 1].remove(key)
            if not self.keys[c - 1]:
                del self.keys[c - 1]

        if c in self.keys:
            self.keys[c].append(key)
        else:
            self.keys[c] = [key]

    def dec(self, key: str) -> None:
        if key in self.count:
            self.count[key] = self.count[key] - 1

        c = self.count[key]
        if c + 1 in self.keys:
            self.keys[c + 1].remove(key)
            if not self.keys[c + 1]:
                del self.keys[c + 1]

        if c == 0:
            del self.count[key]
        else:
            if c in self.keys:
                self.keys[c].append(key)
            else:
                self.keys[c] = [key]

    def getMaxKey(self) -> str:
        if self.keys:
            lst = max(self.keys.keys())
            return self.keys[lst][0]
        else:
            return ""

    def getMinKey(self) -> str:
        if self.keys:
            lst = min(self.keys.keys())
            return self.keys[lst][0]
        else:
            return ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
