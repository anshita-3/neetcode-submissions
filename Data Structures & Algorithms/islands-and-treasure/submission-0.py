class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since shortest distance problem --> use BFS
        
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        # now starting BFS
        while q:
            r,c=q.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue 
                if grid[nr][nc]!=2**31-1:
                    continue 
                grid[nr][nc]=grid[r][c]+1
                q.append((nr,nc))        
    

      

            