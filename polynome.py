class Polynome:

    def __init__(self,coef):
        self.coef = coef

    def afficher(self):
        polynome = ""
        for i in range(len(self.coef)-1,0,-1):
            polynome += f"{self.coef[i]} X^{i} + "
        polynome += f"{self.coef[0]}"  
        print(polynome)
