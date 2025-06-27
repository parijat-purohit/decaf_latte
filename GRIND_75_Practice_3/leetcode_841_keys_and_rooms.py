class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        room_key_list = defaultdict(list)

        for i, keys in enumerate(rooms):
            for k in keys:
                if i != k:
                    room_key_list[i].append(k)
        visited = set()
        room_visit = set([0])
        while room_visit:
            visiting_room = room_visit.pop()
            if visiting_room not in visited:
                visited.add(visiting_room)
                room_visit.update(room_key_list[visiting_room])
        return len(visited) == len(rooms)


s = Solution()
print(s.canVisitAllRooms([[1], [2], [3], [0]]))
print(s.canVisitAllRooms([[2, 3], [], [2], [1, 3]]))
