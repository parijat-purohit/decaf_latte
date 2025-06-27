class TimeMap(object):

    def __init__(self):
        self.timemap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.timemap:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        result = ""
        values = self.timemap.get(key, [])
        l, r = 0, len(values)-1

        while (l <= r):

            m = l + (r-l)//2
            if values[m][1] == timestamp:
                result = values[m][0]
                break
            elif values[m][1] < timestamp:
                result = values[m][0]
                l = m+1
            else:
                r = m-1
        return result


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set('a', 'b', 2)
obj.set('a', 'c', 4)
obj.set('a', 'd', 5)
print(obj.get('a', 4))
print(obj.get('x', 2))
