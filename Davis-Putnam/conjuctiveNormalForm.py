import propositionalLogic as PL

# Conjunctive Normal Form
#   Input: Directed Graph
#   Output: Propositional Encoding in CNF
def propositionalEncoding(fileName):
    # Initialize
    input = open(fileName, "r").read().splitlines()
    clauses = []
    vertices = []
    edges = PL.Edges()

    # Read Input
    for i in input[1:]:
        start, end = i.split()
        if start not in vertices: vertices.append(start)
        if end not in vertices: vertices.append(end)
        edges.add(start, end)
    vertices = sorted(vertices)

    # Encode using Propositions
    clauses += proposition1(vertices)
    clauses += proposition2(vertices)
    clauses += proposition3(vertices, edges)
    clauses += proposition4(vertices)
    clauses += proposition5(vertices)

    outputToFile(vertices, clauses)

def proposition1(vertices):
    # Proposition: Every vertex is traversed at some point in time
    #   i.e. For each vertex 'U' and number of vertices 'N', we have the proposition 'U1 V U2 V ... V UN'
    return [[PL.Atom(True, v, t+1) \
        for t in range(len(vertices))] \
        for v in vertices]
def proposition2(vertices):
    # Proposition: No pair of vertices are traversed at the same time
    #   i.e. For every time 'T' and each pair of vertices 'U' and 'W', we have the proposition '~UT V ~WT'
    return [[PL.Atom(False, u, t+1), PL.Atom(False, w, t+1)] \
        for t in range(len(vertices)) \
        for idx, u in enumerate(vertices) \
        for w in vertices[(idx + 1):]]
def proposition3(vertices, edges):
    # Proposition: Cannot travel between two vertices if there is no edge between them
    #   i.e. For every time 'T' and pair of vertices 'U' and 'W', 
    #      If there is no edge between 'U' and 'W', we have the proposition '~UT V ~W(T+1)'
    return [[PL.Atom(False, u, t+1), PL.Atom(False, w, t+2)] \
        for u in vertices \
        for w in vertices \
        if (u is not w) and (not edges.isIn(u, w)) \
        for t in range(len(vertices)-1)]
def proposition4(vertices):
    # Proposition: There is a vertex at every time
    #   i.e. For every time 'T' and vertices 'U', 'W', 'X', etc, we have the proposition '(U1)T V (U2)T V ... V (UN)T'
    return [[PL.Atom(True, u, t+1) \
        for u in vertices] \
        for t in range(len(vertices))]
def proposition5(vertices):
    # Proposition: No vertex is traversed more than once
    #   i.e. For each vertex 'U' and times 'S' and 'T', we have the proposition '~US V ~UT'
    return [[PL.Atom(False, u, s+1), PL.Atom(False, u, t+1)] \
        for u in vertices \
        for s in range(len(vertices)) \
        for t in range(s+1, len(vertices))]

def outputToFile(vertices, clauses):
    file = open("out/PropositionalEncoding.txt", "w")

    # Build Key
    key = [[v, t+1] for v in vertices for t in range(len(vertices))]

    # Write clauses to file
    for clause in clauses:
        for atom in clause:
            file.write(str((key.index([atom.vertex, atom.time])+1) * (1 if atom.sign else -1)) + ' ')
        file.write('\n') 

    # Write Key to file
    file.write('0\n')
    for i, k in enumerate(key):
        file.write(str(i+1) + ' ' + k[0] + " " + str(k[1]) + '\n')
    
    file.close()