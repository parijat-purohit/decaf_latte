from collections import defaultdict


class UndergroundSystem(object):

    def __init__(self):
        self.system = defaultdict(dict)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if stationName not in self.system:
            self.system[stationName] = {}

        self.system[stationName][id] = t

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if stationName not in self.system:
            self.system[stationName] = {}
        self.system[stationName][id] = t

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        start_stations = self.system[startStation]
        end_stations = self.system[endStation]

        avg_time = 0.0
        cnt = 0.0

        for id, st_time in start_stations.items():
            if id in end_stations and end_stations[id] > st_time:
                avg_time += (end_stations[id] - st_time)
                cnt += 1
        return avg_time/cnt if cnt > 0 else avg_time


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45, "L", 3)
obj.checkIn(32, "P", 8)
obj.checkIn(27, "L", 10)
obj.checkOut(45, "W", 15)
obj.checkOut(27, "W", 20)
obj.checkOut(32, "C", 22)
print(obj.getAverageTime("P", "C"))
print(obj.getAverageTime("L", "W"))
obj.checkIn(10, "L", 24)
print(obj.getAverageTime("L", "W"))
obj.checkOut(10, "W", 38)
print(obj.getAverageTime("L", "W"))
print(obj.getAverageTime("W", "L"))
