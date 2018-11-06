# Davis Putnam Algorithm
#   Input: Propositional Encoding
#   Output: Solution
def davisPutnam():
    # Initialize
    input = open("out/PropositionalEncoding.txt", "r").read().splitlines()
    atoms = {}
    clauses = []
    key = []
    fileSplit = input.index('0')

    # Read File
    for i in input[:fileSplit]:
        c = list(map(int, i.split()))
        clauses.append(c)
        atoms.update(dict.fromkeys(list(map(abs, c)), None))
    for i in input[fileSplit:]:
        key.append(i)

    solution = dpSoft(atoms, clauses)
    outputToFile(solution, key)

def dpSoft(atoms, clauses):
    atomList = [a for c in clauses for a in c]                          # List of Atoms in Clauses
    plList = [True if (k in atomList and -k not in atomList) \
                else False if (k not in atomList and -k in atomList) \
                else None for k,v in atoms.items()]                     # List of Pure Literals
    faList = [c[0] for c in clauses if len(c) == 1]                     # List of Singleton Clauses
    
    # Success: All clauses are satisfied
    if not clauses:
        # Replace None in values with True and return values
        for idx, a in atoms.items():
            atoms[idx] = a if a is not None else True
        return atoms
    # Failure: Some clause in unsatisfiable with current values
    elif [] in clauses:
        return None
    # Pure Literal Elimination
    elif (True in plList) or (False in plList):
        for idx, p in enumerate(plList):
            if p is not None:
                atoms, clauses = propogate(atoms, clauses, idx+1, p)
                return dpSoft(atoms, clauses)
    # Forced Assignment due to Singleton Clause
    elif len(faList) > 0:
        idx = abs(faList[0])
        value = True if faList[0] > 0 else False
        atoms, clauses = propogate(atoms, clauses, idx, value)
        return dpSoft(atoms, clauses)
    else:
        for idx, a in atoms.items():
            if a is None:
                # Try Assigning True
                atoms, newClauses = propogate(atoms, clauses, idx, True)
                newAtoms = dpSoft(atoms, newClauses)
                if newAtoms is not None:
                    return newAtoms
                
                # Try Assigning False
                atoms, newClauses = propogate(atoms, clauses, idx, False)
                newAtoms = dpSoft(atoms, newClauses)
                if newAtoms is not None:
                    return newAtoms
                else:
                    return None

def testUnbound(at, cl):
    # Find Unbound Atom
    for idx, a in at.items():
        if a is None:
            # Try Assigning True
            atoms, clauses = propogate(at, cl, idx, True)
            atoms = dpSoft(atoms, clauses)
            if atoms is not None:
                return atoms
            
            # Try Assigning False
            atoms, clauses = propogate(at, cl, idx, False)
            atoms = dpSoft(atoms, clauses)
            if atoms is not None:
                return atoms
            else:
                return None

def propogate(at, cl, index, value):
    atoms = dict(at)
    clauses = cl.copy()
    checkValue = index if value else -index

    # Assign atom value
    atoms[index] = value
    # Delete every clause where value appears
    clauses = [c for c in clauses if checkValue not in c]
    # Delete every literal where ~value appears
    clauses = [[a for a in c if -checkValue != a] for c in clauses]

    return atoms, clauses

def outputToFile(solution, key):
    file = open("out/DavisPutnam.txt", "w")

    # Write solution to file
    if solution is not None:
        for atom, value in solution.items():
            file.write(str(atom) + " " + ("T" if value else "F") + "\n")
    for k in key:
        file.write(k + "\n")

