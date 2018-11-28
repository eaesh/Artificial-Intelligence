import sys
import training

lines = sys.argv[1]
isSummary = True if len(sys.argv) > 2 else False
sentences = open('in/input.txt', 'r').read().splitlines()
#occurr = dict()
#tRules = dict()
rules = []

# Training
for s in sentences[:int(lines)]:
    tree = training.sentenceToTree(s.split())[0]
    rules += training.readTree(tree)
    print("Tree:", tree)

rules = training.train(rules)

print()
print("Rules:")
for r in rules:
    print(r)