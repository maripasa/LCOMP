"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """

from formula import Formula, Atom, Not, Or, And, Implies

def length(formula: Formula) -> int:
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, (Or, And, Implies)):
        return length(formula.left) + length(formula.right) + 1
    raise ValueError


def subformulas(formula: Formula) -> set[Formula]:
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, (Or, And, Implies)):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)
    raise ValueError

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula: Formula) -> set[Atom]:
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, (Or, And, Implies)):
        return atoms(formula.left).union(atoms(formula.right))
    raise ValueError

def number_of_atoms(formula: Formula) -> int:
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """

    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, (Or, And, Implies)):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)
    raise ValueError

def number_of_connectives(formula: Formula) -> int:
    """Returns the number of connectives occurring in a formula."""
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner) + 1
    if isinstance(formula, (Or, And, Implies)):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right) + 1
    raise ValueError

def is_literal(formula: Formula) -> bool:
    """Returns True if formula is a literal. It returns False, otherwise"""
    if isinstance(formula, Atom):
        return True
    if isinstance(formula, Not):
        return isinstance(formula.inner, Atom)
    return False

def substitution(formula: Formula, old_subformula: Formula, new_subformula: Formula) -> Formula:
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""

    if formula == old_subformula:
        return new_subformula

    if isinstance(formula, Atom):
        return formula
    
    if isinstance(formula, Not):
        formula.inner = substitution(formula.inner, old_subformula, new_subformula)
        return formula

    if isinstance(formula, (Or, And, Implies)):
        formula.left = substitution(formula.left, old_subformula, new_subformula)
        formula.right = substitution(formula.right, old_subformula, new_subformula)
        return formula
        
    raise ValueError
    
def is_clause(formula: Formula) -> bool:
    """Returns True if formula is a clause. It returns False, otherwise"""
    if is_literal(formula):
        return True
    if isinstance(formula, Or):
        return is_clause(formula.left) and is_clause(formula.right)
    return False

def is_nnf(formula: Formula) -> bool:
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    if is_literal(formula):
        return True
    if isinstance(formula, (Or, And)):
        return is_nnf(formula.left) and is_nnf(formula.right)
    return False

def is_cnf(formula: Formula) -> bool:
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    if is_clause(formula):
        return True
    if isinstance(formula, And):
        return is_cnf(formula.left) and is_cnf(formula.right)
    return False

def is_term(formula: Formula) -> bool:
    """Returns True if formula is a term. It returns False, otherwise"""
    if is_literal(formula):
        return True
    if isinstance(formula, And):
        return is_term(formula.left) and is_term(formula.right)
    return False

def is_dnf(formula: Formula) -> bool:
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    if is_term(formula):
        return True
    if isinstance(formula, Or):
        return is_dnf(formula.left) and is_dnf(formula.right)
    return False

def is_dnnf(formula: Formula) -> bool:
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    if is_nnf(formula):
        if isinstance(formula, And):
            if not (atoms(formula.left) & atoms(formula.right)):
                return True
            return is_dnnf(formula.right) and is_dnnf(formula.left)
        if isinstance(formula, Or):
            return is_dnnf(formula.right) and is_dnnf(formula.left)
    return False
