from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        # reverse sort so we can pop() the smallest lexicographic next
        for src in graph:
            graph[src].sort(reverse=True)

        route = []

        def visit(airport: str):
            while graph[airport]:
                nxt = graph[airport].pop()   # smallest due to reverse sort
                visit(nxt)
            route.append(airport)            # add when no outgoing edges left

        visit("JFK")
        return route[::-1]