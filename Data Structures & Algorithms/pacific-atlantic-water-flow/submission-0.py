class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()

        def dfs(r,c,ocean):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if (r,c) in ocean:
                return
            ocean.add((r,c))
            dirs=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dirs:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue 
                if heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,ocean)
        
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        
        return [[r,c] for r,c in pacific & atlantic]