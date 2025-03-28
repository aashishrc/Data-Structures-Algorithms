class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: if grid is empty
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            visited[r][c] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # IMPORTANT: check '1' as a string, not integer
                    if grid[nr][nc] == "1" and not visited[nr][nc]:
                        dfs(nr, nc)

        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                # Also check "1" as a string
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1

        return island_count
