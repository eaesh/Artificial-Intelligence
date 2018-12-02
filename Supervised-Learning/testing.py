class Tree:
    def __init__(self, ntp, sp, ep, w, l, r, p):
        self.nonTermPhrase = ntp
        self.startPhrase = sp
        self.endPhrase = ep
        self.word = w
        self.leftTree = l
        self.rightTree = r
        self.prob = p
    
    def __repr__(self):
        return "( " + self.nonTermPhrase + "\t" + str(self.startPhrase) + "\t" + str(self.endPhrase) + "\t" + str(self.word) \
            + "\t" + str(self.leftTree) + "\t" + str(self.rightTree) + "\t" + str(self.prob) + " )"

def readSentence(sentence):
    return [s for s in sentence.split() if (s[0] != "*") and (s[0] != "+")]

def cykParser(rules, sentence):
    grammar = []
    lexicon = []
    P = {}

    # Read through Rules
    for r in rules:
        P.setdefault(r[0], [[None for _ in range(len(sentence))] for _ in range(len(sentence))])
        if len(r) == 4:
            grammar.append(r)
        else:
            lexicon.append(r)

    # Identify parts of speech
    for i, word in enumerate(sentence):
        matches = [l for l in lexicon if word == l[1]]
        # Create Tree for each match
        for m in matches:
            P[m[0]][i][i] = Tree(m[0], i, i, m[1], None, None, m[2])

    # Populate Trees
    for length in range(2, len(sentence) + 1):
        for i in range(0, len(sentence) + 1 - length):
            j = i + length - 1
            for pos in P:
                P[pos][i][j] = Tree(pos, i, j, None, None, None, 0.0)
                for k in range(i, j):
                    applyRules = [g for g in grammar if g[0] == pos]
                    for rule in applyRules:
                        M = P[pos][i][j]
                        Y = P[rule[1]][i][k]
                        Z = P[rule[2]][k+1][j]
                        if Y is not None and Z is not None:
                            newProb = Y.prob * Z.prob * rule[3]
                            if newProb > M.prob:
                                M.leftTree = Y
                                M.rightTree = Z
                                M.prob = newProb

    # Find Most Probable Tree
    MPT = P["S"][0][len(sentence)-1]
    if MPT.prob > 0:
        return treeToSentence(MPT)
    else:
        return "This sentence cannot be parsed."

def treeToSentence(tree):
    sentence = ""
    if tree.word is None:
        sentence += "*" + tree.nonTermPhrase
        sentence += " " + treeToSentence(tree.leftTree)
        sentence += " " + treeToSentence(tree.rightTree)
    else:
        sentence += "+" + tree.nonTermPhrase
        sentence += " " + tree.word
    return sentence