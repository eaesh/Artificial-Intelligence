# Davis Putnam Algorithm
#   Input: Propositional Encoding
#   Output: Solution
def davisPutnam():
    input = open("out/PropositionalEncoding.txt", "r").read().splitlines()
    
    for i in input:
        print(i.rstrip().split(" "))