class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for course, prereq in prerequisites:
            if prereq not in adj:
                adj[prereq] = []
            adj[prereq].append(course)

        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            if course not in adj:
                return True

            path.add(course)

            for next_course in adj[course]:
                if not dfs(next_course):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True