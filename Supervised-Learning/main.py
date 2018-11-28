import sys
import grammar

def fudge():
    return [1, 2]

sentences = open('in/input.txt', 'r').read().splitlines()
lines = sys.argv[1]
isSummary = True if len(sys.argv) > 2 else False
rules = []

for s in sentences[:int(lines)]:
    tree = grammar.sentenceToTree(s.split())[0]
    print("Tree:", tree)
    grammar.parseTree(tree, rules)
    #print("New Rules:", rules)

    #for n in newRules:
     #   isIn = False
      #  for r in rules:
       #     if n == r[0]:
        #        r[1] += 1
         #       isIn = True
          #      break
        
        #if not isIn:
         #   rules.append([n, 1])

print()    
print("Rules:", rules)

#print(rules.index([['S', 'Noun', 'VP'], 1]))