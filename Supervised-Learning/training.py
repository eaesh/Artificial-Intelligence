# Convert sentence to tree in array form
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

# Get Rules from tree
def getRules(tree):
    rules = []
    if len(tree) == 3:
        # Phrase Marker
        rules.append(tree[0])
        rules.append([tree[0], tree[1][0], tree[2][0]])
        rules += getRules(tree[1]) + getRules(tree[2])
    elif len(tree) == 2:
        # Part of Speech
        rules.append(tree[0])
        rules.append([tree[0], tree[1]])
    return rules

# Train program and get probabilities for rules
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