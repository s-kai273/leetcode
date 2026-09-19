from collections import deque


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat_count = 0
        people.sort()
        people = deque(people)
        while people:
            lp_weight = people.pop()
            sp_weight = people[0] if len(people) > 0 else 0
            # Operation should be implemented
            # boat_count should be incremented
            if lp_weight + sp_weight <= limit:
                if len(people) > 0:
                    people.popleft()
            boat_count += 1
        return boat_count
