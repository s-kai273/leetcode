class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = dict()
        for from_airport, to_airport in sorted(tickets, reverse=True):
            graph.setdefault(from_airport, list()).append(to_airport)

        def dfs(airport: str):
            while airport in graph and graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)

        itinerary = list()
        dfs("JFK")
        return itinerary[::-1]
