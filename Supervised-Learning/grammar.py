def sentenceToTree(sentence):
    node = sentence[0]

    if node[0] == '*':
        part1, sent = sentenceToTree(sentence[1:])
        part2, sent2 = sentenceToTree(sent)
        return [[node[1:], part1, part2], sent2]
    elif node[0] == '+':
        [result, sent] = sentenceToTree(sentence[1:])
        return [[node[1:], result], sent]
    else:
        return [node, sentence[1:]]

def parseTree(tree, rules):
    if len(tree) == 3:
        # Grammar
        addRule([tree[0], tree[1][0], tree[2][0]], rules)
        parseTree(tree[1], rules)
        parseTree(tree[2], rules)
    elif len(tree) == 2:
        # Lexicon
        addRule([tree[0], tree[1]], rules)
    return rules

def addRule(newRule, rules):
    isIn = False
    for r in rules:
        if newRule in r:
            r[1] += 1
            isIn = True
            break
    
    if not isIn:
        rules.append([newRule, 1])

def printTree(tree, tab = 0):
    print(tab*'\t', tree[0])
    tab += 1
    for t in tree[1:]:
        if len(t) == 2:
            print(tab * '\t', t[0], '\t', t[1])
        else:
            printTree(t, tab)