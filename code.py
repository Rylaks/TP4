from polynome import *
from arbre import *
from noeud import *

p = Polynome([0.1,0.1,-1.3,-0.1,1.2])
p.afficher()

#Ex 2:
n1 = Noeud("mul",[3,"sin(x)"])
n1.afficher()

n2 = Noeud("exp",Noeud("add",[2,"y"]))
n2.afficher()

a1 = Arbre("sub",[])
