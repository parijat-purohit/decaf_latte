class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        result = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = l + (r-l)//2
            if values[m][1] == timestamp:
                result = values[m][0]
                break
            elif values[m][1] < timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result


t = TimeMap()
t.set('a', 'alpha', 2)
t.set('a', 'beta', 4)
t.set('a', 'gamma', 5)
print(t.get('a', 5))
