import knapsack
import iterativeDeepening
import hillClimbing
import random

# Initialize
input = open("in/input4.txt", "r").read().splitlines()
targetValue, maxWeight = [float(i) for i in input.pop(0).split()]
items=[]

# Fill Items
for i in input:
    name, value, weight = [j for j in i.split()]
    items.append(knapsack.Item(name, float(value), float(weight)))

# Iterative Deepening Algorithm
#iterativeDeepening.solve(targetValue, maxWeight, items)

# Hill Climbing Algorithm
hillClimbing.solve(targetValue, maxWeight, items)