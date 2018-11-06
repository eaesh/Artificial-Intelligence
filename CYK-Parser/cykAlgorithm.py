class Tree:
    def __init__(self, ntp, sp, ep, w, l, r, p):
        self.nonTermPhrase = ntp
        self.startPhrase = sp
        self.endPhrase = ep
        self.word = w
        self.leftTree = l
        self.rightTree = r
        self.prob = p

def printTree(tree, indent = 0):
    node = "\t" * indent + tree.nonTermPhrase
    if tree.word is not None:
        node += "\t" + tree.word
    print(node)


    if tree.leftTree is not None:
        printTree(tree.leftTree, indent + 1)
    if tree.rightTree is not None:
        printTree(tree.rightTree, indent + 1)

def findMostProbableTree(phrase, ruleFile):
    grammarRules = []
    posRules = []
    P = {}

    # Read through Rules
    for r in ruleFile:
        newRule = r.split()
        newRule.remove('->')
        newRule[len(newRule)-1] = float(newRule[len(newRule)-1][1:-1])
        P.setdefault(newRule[0], [[None for _ in range(len(phrase))] for _ in range(len(phrase))])
        if len(newRule) > 3:
            grammarRules.append(newRule)
        else:
            posRules.append(newRule)

    # Identify Parts of Speech
    for i in range(len(phrase)):
        matches = [r for r in posRules if phrase[i] == r[1]]
        for m in matches:
            pos, word, prob = m
            P[pos][i][i] = Tree(pos, i, i, word, None, None, prob)

    # Populate Trees
    for length in range(2, len(phrase) + 1):
        for i in range(0, len(phrase) + 1 - length):
            j = i + length - 1
            for pos in P:
                P[pos][i][j] = Tree(pos, i, j, None, None, None, 0.0)
                for k in range(i, j):
                    applicableRules = [r for r in grammarRules if r[0] == pos]
                    for rule in applicableRules:
                        M = P[pos][i][j]
                        Y = P[rule[1]][i][k]
                        Z = P[rule[2]][k+1][j]
                        if Y is not None and Z is not None:
                            newProb = Y.prob * Z.prob * rule[3]
                            if newProb > M.prob:
                                M.leftTree = Y
                                M.rightTree = Z
                                M.prob = newProb

    # Print Most Probable Tree
    MPT = P["S"][0][len(phrase)-1]
    if MPT.prob > 0:
        printTree(MPT)
        print("Probability =", MPT.prob)
    else:
        print("This sentence cannot be parsed")