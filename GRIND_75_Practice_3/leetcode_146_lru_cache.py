class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            v = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = v
            return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            k = next(iter(self.cache))
            self.cache.pop(k)
        self.cache[key] = value


s = LRUCache(2)
s.put(1, 1)
s.put(2, 2)
print(s.get(1))
s.put(3, 3)
print(s.get(2))
s.put(4, 4)
print(s.get(1))
print(s.get(3))
print(s.get(4))
