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

def readTree(tree):
    rules = []
    if len(tree) == 3:
        # Phrase Marker
        rules.append(tree[0])
        rules.append([tree[0], tree[1][0], tree[2][0]])
        rules += readTree(tree[1]) + readTree(tree[2])
    elif len(tree) == 2:
        # Part of Speech
        rules.append(tree[0])
        rules.append([tree[0], tree[1]])
    return rules

def train(newRules):
    occur = dict()
    tRules = dict()
    rules = []
    
    # Read new rules
    for n in newRules:
        if isinstance(n, str):
            if n in occur.keys():
                occur[n] += 1
            else:
                occur[n] = 1
        else:
            r = ' '.join(n)
            if r in tRules.keys():
                tRules[r] += 1
            else:
                tRules[r] = 1

    # Find Probabilities
    for tRule, count in tRules.items():
        rule = tRule.split()
        phraseMarker = rule[0]
        rules.append(rule + [count/occur[phraseMarker]])
    return rules

def printTree(tree, tab = 0):
    print(tab*'\t', tree[0])
    tab += 1
    for t in tree[1:]:
        if len(t) == 2:
            print(tab * '\t', t[0], '\t', t[1])
        else:
            printTree(t, tab)