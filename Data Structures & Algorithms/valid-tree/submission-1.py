class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        # adj={}
        # for a,b in edges:
        #     if a not in adj:
        #         adj[a]=[]
        #     if b not in adj:
        #         adj[b]=[]
        #     adj[a].append(b)
        #     adj[b].append(a)
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited=set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)
        # if len(visited)==n:
        #     return True 
        # return False
        return len(visited)==n