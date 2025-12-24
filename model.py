import random

class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6 #Vite massime
        self._T = self._TMax #Vite restanti
        self._segreto = None

    def reset(self):
        #Questo metodo resetta il gioco, in quasiasi momento.
        self._segreto = random.randint(0,self._NMax)
        self._T = self._TMax
        print(self._segreto)

    def play(self,guess):
        #da fuori ci arriva un tentativo, confrontiamo il tentativo con il segreto.
        self._T -= 1
        if guess == self._segreto:
            return 0 #ho vinto
        if self._T == 0:
            return 2 #ho finito le vite
        if guess > int(self._segreto):
            return -1 #il segreto è più piccolo
        return 1 #il segreto è più grande



if __name__=="__main__":
    m = Model()
    m.reset()
    print(m.play(50))





