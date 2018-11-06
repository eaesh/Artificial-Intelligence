import conjuctiveNormalForm as CNF
import davisPutnam as DP
import formatOutput as FO

# Initialize
fileName = "in/input2.txt"

# Part 1: Propositional Encoding in CNF
CNF.propositionalEncoding(fileName)

# Part 2: Davis-Putnam Algorithm
DP.davisPutnam()

# Part 3: Format Output and Write to File
FO.writeOutput()