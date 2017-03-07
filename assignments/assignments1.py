v = open('values.txt','r').read()
class Abacus():
    """def __init__(self,  key):
        self.key = key"""
    def add(self, original, val):
        y=[]
        z=[]
        for i in original:
            y.append(str(9-i.find('---')))
        s=map(str, str(int(''.join(y))+val))
        for i in s:
           z.append((9-int(i))*'o'+'---'+int(i)*'o')
        return z
class CrossWord():
    def countWords(self, board, size):
        f=0
        for i in board:
            x=i.split("X")
            f=f+x.count(('.'*size))
        return f
class WordFind():
    def findWords(self, grid, wordList):
        pass
class EventOrder():
    def getCount(self, longEvents, instantEvents):
        pass

