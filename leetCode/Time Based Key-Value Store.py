"""
The `TimeMap` class maintains a time-based key-value data structure using a dictionary (`timestamps`). 
The class provides methods to set key-value pairs with timestamps (`set`) and retrieve values at a specific timestamp (`get`). 

The algorithm utilizes binary search within the timestamp-value pairs associated with each key, ensuring efficient retrieval of the most recent value at or before the target timestamp. 

The design allows for storing multiple values for the same key at different timestamps.
"""
class TimeMap:

    def __init__(self):
        self.timestamps: dict[list[list]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.timestamps[key]
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                res = values[mid][1]
                l = mid + 1
        return res
