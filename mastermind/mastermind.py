
import sys
class Mastermind():
    def __init__(self):
        self._target = [3,7,6,5]

    def play(self, num):
        if len(num) != len(self._target):
            return False
        return self._target == num
    def exist(self,num):
        cont=0
        for i in num:
            if i in self._target:
                cont+=1
        return cont

    def exact(self,num):
        cont=0
        pos = 0
        for i in num:
            if i == self._target[pos]:
                cont+=1
            pos+=1
        return cont
#   m = Mastermind()
#print(m.play(int(sys.argv[1])))

