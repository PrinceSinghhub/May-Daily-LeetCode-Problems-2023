class Solution:

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = collections.deque([i])
                while q:
                    cur = q.pop()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True