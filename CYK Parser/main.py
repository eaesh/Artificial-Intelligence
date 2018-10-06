import cykAlgorithm

# Initialize   
phrases = open("phrases.txt", "r").read().splitlines() 
ruleFile = open("grammar.txt", "r").read().splitlines()

for p in phrases:
    print(p)
    cykAlgorithm.findMostProbableTree(p.lower().split(), ruleFile)
    print("---------------------------------")
