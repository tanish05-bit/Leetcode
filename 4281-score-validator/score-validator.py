class Solution(object):
    def scoreValidator(self, events):
        score=0
        counter=0
        for i in events:
            if i=="W":
                counter+=1
                if counter==10:
                    break
            elif i=="WD":
                score+=1
            elif i=="NB":
                score+=1
            else:
                score+=int(i)
        return [score,counter]        


        