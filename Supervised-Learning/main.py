import sys
import training
import testing

def main():
    sentences = open('in/input2.txt', 'r').read().splitlines()
    lines = sys.argv[1]
    isSummary = True #if len(sys.argv) > 2 else False
    rules = []

    # Training
    for s in sentences[:int(lines)]:
        tree = training.sentenceToTree(s.split())[0]
        rules += training.getRules(tree)

    # Print Rules
    rules = training.train(rules)
    printRules(rules)

    # Testing
    correct = 0
    total = len(sentences[int(lines):])
    if total > 0:
        if isSummary:
            print()
            print("Phrases:")
        for s in sentences[int(lines):]:
            sent = testing.cykParser(rules, testing.readSentence(s))
            correct += 1 if sent == s.strip() else 0
            if isSummary:
                print(sent, "Right" if sent == s.strip() else "Wrong")
        
        print()
        print(f"Accuracy: The parse was tested on {total} sentences. It got {correct}, for an accuracy of {correct/total}.")
    else:
        print()
        print("No tests to run.")

def printRules(rules):
    # Find grammar and lexicon from rules
    grammar = [r for r in rules if len(r) == 4]
    grammar = sorted(grammar, key=lambda r: (len(r[0]), r[0]))
    lexicon = [r for r in rules if len(r) == 3]
    lexicon = sorted(lexicon, key=lambda r: (len(r[0]), r[0], r[1]))

    # Print
    print("Grammar")
    for g in grammar:
        print(f"{g[0]} -> {g[1]} {g[2]} [{round(g[3], 4)}]")
    print()
    print("Lexicon")
    for l in lexicon:
        print(f"{l[0]} -> {l[1]} [{round(l[2], 4)}]")

main()