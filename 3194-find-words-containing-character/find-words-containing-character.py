class Solution(object):
    def findWordsContaining(self, words, x):
        L=[]
        for i in range(len(words)):
            if x in words[i]:
                L.append(i)
        return(L)
        