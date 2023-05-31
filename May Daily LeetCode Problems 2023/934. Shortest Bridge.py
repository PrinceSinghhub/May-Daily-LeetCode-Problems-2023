class Solution:
    def isBoundary(self, grid, point) -> bool:
        x, y = point[0], point[1]
        if x - 1 < 0 or y - 1 < 0 or x + 1 >= len(grid) or y + 1 >= len(grid[x]): return True
        if grid[x - 1][y] == 1: return True
        if grid[x + 1][y] == 1: return True
        if grid[x][y - 1] == 0: return True
        if grid[x][y + 1] == 0: return True
        return False

    def dfs(self, grid, start, visited):
        x, y = start[0], start[1]
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]) or grid[x][y] != 1: return
        if start not in visited:
            visited.add(start)
            self.dfs(grid, (x + 1, y), visited)
            self.dfs(grid, (x, y + 1), visited)
            self.dfs(grid, (x - 1, y), visited)
            self.dfs(grid, (x, y - 1), visited)

    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find the shortest distance between 2 disconnected components
        island1, island2, positionsOfLand = set(), set(), set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1: positionsOfLand.add((x, y))

        for each in positionsOfLand:
            self.dfs(grid, each, island1)
            break

        for each in positionsOfLand - island1:
            self.dfs(grid, each, island2)
            break

        boundary1 = [each for each in island1 if self.isBoundary(grid, each)]
        boundary2 = [each for each in island2 if self.isBoundary(grid, each)]

        answer = float("inf")
        for each1 in boundary1:
            for each2 in boundary2:
                x1, y1 = each1[0], each1[1]
                x2, y2 = each2[0], each2[1]
                answer = min(answer, (abs(x1 - x2) + abs(y1 - y2) - 1))
                if answer == 1: break
        return answer