class Noeud:

    def __init__(self, nom, enfants):
        self.nom = nom
        self.enfants = enfants

    def ajouter_enfant(self,enfant):
        self.enfants.append(enfant)

    def afficher(self):
        print(self.nom, end='')
        print("(", end ='')
        for k in range(len(self.enfants)):
            if k < len(self.enfants) - 1:
                print(str(self.enfants[k]) + ", ", end='')
            else:
                print(str(self.enfants[k]), end='')
        print(")")