# 146. LRU Cache

# Approach 1. OrderedDict
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            value = self.cache.pop(key)
            self.cache[key] = value         # newly add recently used data -> becomes last
            return value
        except KeyError:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # last=False pops first item
        self.cache[key] = value
        