import knapsack
import random

def solve(targetValue, maxWeight, items):    
    solutions = []
    
    # 10 Random Restarts
    for i in range(0, 10):
        currState = knapsack.Knapsack()
        for item in items:
            if random.randint(0, 1) == 0:
                currState = currState.add(item)
            
        nextState = None
        while True:
            nextState = findBestNeighbor(targetValue, maxWeight, items, currState)
            if (currState != nextState):
                currState = nextState
            else:
                solutions.append(currState)
                break

    # Print Solution
    minErr = float('inf')
    minState = None
    for s in solutions:
        err = calcError(s, targetValue, maxWeight)
        if err < minErr and s.totalWeight <= maxWeight and s.totalValue >= targetValue:
            minErr = err
            minState = s
    
    if minState is not None:
        minState.print()
        print("Target Value:", targetValue, "| Max Weight:", maxWeight)
    else:
        print("No Solution")


def findBestNeighbor(targetValue, maxWeight, items, currState):
    # Find Neighbors and Evaluate Error
    neighbors = findNeighbors(currState, items)
    minErr = calcError(currState, targetValue, maxWeight)

    for n in neighbors:
        err = calcError(n, targetValue, maxWeight)
        if err < minErr:
            minErr = err
            currState = n
    return currState

def findNeighbors(knapsack, items):
    neighbors = []

    for item in items:
        if not knapsack.isIn(item):
            # Add Item
            neighbors.append(knapsack.add(item))
        else:
            # Remove Item
            neighbors.append(knapsack.remove(item))

            # Replace Item
            for newItem in items:
                if not knapsack.isIn(newItem):
                    neighbors.append(knapsack.add(newItem).remove(item))
    return neighbors

def calcError(knapsack, targetValue, maxWeight):
    return max(knapsack.totalWeight - maxWeight, 0) + max (targetValue - knapsack.totalValue, 0)