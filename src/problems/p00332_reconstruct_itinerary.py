class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        path_dict = dict()

        # Convert tickets into path_dict
        for source, dist in tickets:
            path_dict.setdefault(source, dict())
            path_dict[source][dist] = path_dict[source].get(dist, 0) + 1

        # Define dfs which updates path to store valid airports
        def dfs(source: str | None, dist: str, path: list):
            path.append(dist)
            path_dict[source][dist] -= 1
            source = dist
            if source not in path_dict:
                return
            for dist in sorted(path_dict[source].keys()):
                if path_dict[source][dist] > 0:
                    dfs(source, dist, path)
                    if len(path) == len(tickets) + 1:
                        break
                    path.pop()
                    path_dict[source][dist] += 1

        path_dict[None] = {"JFK": 1}
        itinerary = list()
        dfs(None, "JFK", itinerary)
        return itinerary
