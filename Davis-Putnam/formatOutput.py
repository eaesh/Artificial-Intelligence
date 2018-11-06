# Format Output
#   Input: Davis Putnam Algorithm Results
#   Output: Solution to Hamiltonian Path 
def writeOutput():
    # Initialize
    input = open("out/DavisPutnam.txt", "r").read().splitlines()
    fileSplit = input.index("0")
    dpAnswer = {}
    key = {}
    solution = {}
    output = []

    # Read File
    for i in input[:fileSplit]:
        a = i.split(" ")
        dpAnswer.update({ int(a[0]): a[1] })
    for i in input[fileSplit+1:]:
        k = i.index(" ")
        key.update({ int(i[:k]): i[k+1:] })

    # Find Path
    for idx, k in key.items():
        if dpAnswer[idx] == 'T':
            pos = k.split(" ")
            solution.update({ int(pos[1]): pos[0] })
    for i in range(1, len(solution)+1):
        output.append(solution[i])

    # Write to File
    file = open("out/Output.txt", "w")
    file.write(" -> ".join(output))