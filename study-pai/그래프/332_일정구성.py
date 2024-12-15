from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        # If there are multiple valid itineraries, 
        # you should return the itinerary that has the smallest lexical order when read as a single string.
        graph = defaultdict(list)  # use list as stack
        for dept, arrival in sorted(tickets, reverse=True):
            graph[dept].append(arrival)

        ans = []

        def dfs(dept):
            while graph[dept]:
                arrival = graph[dept].pop()
                dfs(arrival)
            # Append elements from the last arrival
            ans.append(dept)

        # All of the tickets belong to a man who departs from "JFK"
        dfs("JFK")
        return ans[::-1]


assert Solution().findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
