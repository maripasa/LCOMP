"""This module is designed to define formulas in propositional logic.
For example, the following piece of code creates an object representing (p v s).

formula1 = Or(Atom('p'), Atom('s'))


As another example, the piece of code below creates an object that represents (p → (p v s)).

formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
"""

class Formula:
    def __init__(self):
        pass

class Atom(Formula):
    """
    This class represents propositional logic variables.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return str(self.name)

    def __eq__(self, other) -> bool:
        return isinstance(other, Atom) and other.name == self.name

    def __hash__(self):
        return hash((self.name, 'atom'))

class Implies(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'implies'))

class Not(Formula):
    def __init__(self, inner: Formula):
        super().__init__()
        self.inner = inner

    def __repr__(self) -> str:
        return "(" + u"\u00ac" + str(self.inner) + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, Not) and other.inner == self.inner

    def __hash__(self):
        return hash((hash(self.inner), 'not'))

class And(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, And) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'and'))

class Or(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, Or) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'or'))

class Iff:
    """
    Describes the 'if and only if' logical connective (<->) from propositional logic.
    Unicode value for <-> is 2194.
    """
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2194" + " " + self.right.__str__() + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, Iff) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'iff'))

class Xor:
    """
    Describes the xor (exclusive or) logical connective from propositional logic.
    Unicode value for xor is 2295.
    """
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2295" + " " + self.right.__str__() + ")"

    def __eq__(self, other) -> bool:
        return isinstance(other, Xor) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'xor'))
