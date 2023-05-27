import random
from typing import List

from CSP.Problem import Problem
from CSP.Variable import Variable
from king.KingConstraint import PotionNotSameConstraint


class KingProblem(Problem):

    def __init__(self):
        super().__init__([], [], "King Problem")

        al = Variable[str]([['trans', 'blue'], ['trans', 'black'], ['trans', 'purple']], 'aldo')
        bt = Variable[str]([['trans', 'blue'], ['poison', 'blue'], ['invisible', 'blue'], ['heal', 'blue']], 'beatrice')
        ig = Variable[str]([['poison', 'blue'], ['poison', 'green'], ['poison', 'red']], 'ignatius')
        lo = Variable[str]([['invisible', 'green'], ['trans', 'green'], ['heal', 'green'], ['acid', 'green']], 'lorenzo')
        os = Variable[str]([['invisible', 'green'], ['invisible', 'red'], ['invisible', 'purple']], 'orsola')

        c1 = PotionNotSameConstraint([al, bt])
        c2 = PotionNotSameConstraint([al, ig])
        c3 = PotionNotSameConstraint([al, lo])
        c4 = PotionNotSameConstraint([al, os])
        c5 = PotionNotSameConstraint([bt, ig])
        c6 = PotionNotSameConstraint([bt, lo])
        c7 = PotionNotSameConstraint([bt, os])
        c8 = PotionNotSameConstraint([ig, lo])
        c9 = PotionNotSameConstraint([ig, os])
        c10 = PotionNotSameConstraint([lo, os])

        self.constraints = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

        self.variables = [al, bt, ig, lo, os]
