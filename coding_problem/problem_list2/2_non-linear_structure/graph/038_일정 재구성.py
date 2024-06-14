from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def DFS(start):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[start]:
                DFS(graph[start].pop(0))
            route.append(start)

        DFS("JFK")

        # 다시 뒤집어서 어휘순 결과로
        return route[::-1]