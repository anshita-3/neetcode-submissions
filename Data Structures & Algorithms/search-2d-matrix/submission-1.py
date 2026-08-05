class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l=0
        # rows=len(matrix)
        # cols=len(matrix[0])
        # r=rows*col-1
        # while l<=r:
        #     m=(l+r-1)//2

        for i in matrix:
            for j in i:
                if j==target:
                    return True 
        return False 