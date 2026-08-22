class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=set()
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count 

        