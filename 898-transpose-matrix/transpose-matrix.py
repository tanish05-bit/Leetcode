class Solution(object):
    def transpose(self, matrix):
        return([i for i in zip(*matrix)])