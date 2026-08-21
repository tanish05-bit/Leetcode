class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        L=moves.count('L')
        R=moves.count('R')
        U=moves.count('_')
        return (abs(L-R)+U)
        