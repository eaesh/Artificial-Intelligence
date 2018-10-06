import knapsack

def solve(targetValue, maxWeight, items):
    stateSpace = getStateSpace(knapsack.Knapsack(), maxWeight, items)
    solution = getSolution(targetValue, stateSpace)
    if solution is not None:
        print([item.name for item in solution.items])
    else:
        print("No Solution")

def getStateSpace(knapsack, maxWeight, items, index = 0):
    newStates = []
    for item in items[index:]:
        if knapsack.meetsWeight(item, maxWeight) and not knapsack.isIn(item):
            newKnapSack = knapsack.add(item)
            newStates.append(newKnapSack)
            newStates += getStateSpace(newKnapSack, maxWeight, items, items.index(item))
    return newStates

def getSolution(targetValue, stateSpace):
    for knapsack in stateSpace:
        if knapsack.totalValue >= targetValue:
            return knapsack
    return None

def printStateSpace(stateSpace):
    for state in stateSpace:
        print([item.name for item in state.items], state.totalValue, state.totalWeight)