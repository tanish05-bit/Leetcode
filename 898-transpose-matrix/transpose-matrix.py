class Solution(object):
    def transpose(self, matrix):
        transpose=[]
        for i in range(len(matrix[0])):
            transpose.append([0]*len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i]=matrix[i][j]
        return(transpose)