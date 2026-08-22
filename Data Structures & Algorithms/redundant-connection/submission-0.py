class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(len(edges)+1)]
        # for a,b in edges:
        #     adj[a].append(b)
        #     adj[b].append(a)

        def dfs(node,target,visited):
            if node==target:
                return True 
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei,target,visited):
                        return True 
            return False
        
        for a,b in edges:
            visited=set()
            if dfs(a,b,visited):
                return [a,b]
            adj[a].append(b)
            adj[b].append(a)
