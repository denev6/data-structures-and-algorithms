class Solution:
    def __init__(self):
        self._grid = []
        self._visited = []
        self._m = 0
        self._n = 0

    def numIslands(self, grid) -> int:
        # init
        num_land = 0
        self._grid = grid
        self._m = len(grid)
        self._n = len(grid[0])
        self._visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # visit lands only
        for i in range(self._m):
            for j in range(self._n):
                if not self._visited[i][j] and self._grid[i][j] == "1":
                    num_land += 1
                    self.visit(i, j)

        return num_land

    def visit(self, i, j):
        # visit adjacent land with dfs
        self._visited[i][j] = True

        # up
        if i > 0 and not self._visited[i - 1][j] and self._grid[i - 1][j] == "1":
            self.visit(i - 1, j)
        # down
        if (
            i < self._m - 1
            and not self._visited[i + 1][j]
            and self._grid[i + 1][j] == "1"
        ):
            self.visit(i + 1, j)
        # left
        if j > 0 and not self._visited[i][j - 1] and self._grid[i][j - 1] == "1":
            self.visit(i, j - 1)
        # right
        if (
            j < self._n - 1
            and not self._visited[i][j + 1]
            and self._grid[i][j + 1] == "1"
        ):
            self.visit(i, j + 1)