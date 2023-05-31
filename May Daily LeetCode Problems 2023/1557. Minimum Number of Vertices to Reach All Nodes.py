class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        path = set(range(n))

        for key, val in edges:
            if val in path:
                path.remove(val)

        path = list(path)
        return path
