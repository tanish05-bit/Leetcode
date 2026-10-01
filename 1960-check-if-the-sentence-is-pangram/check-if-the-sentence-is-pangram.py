class Solution(object):
    def checkIfPangram(self, sentence):
        a=len(set(sentence))
        return(bool(a==26))