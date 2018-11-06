# Item Class
class Item:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

# Knapsack Class
class Knapsack:
    def __init__(self, i = [], tV = 0, tW = 0):
        self.items = i
        self.totalValue = tV
        self.totalWeight = tW

    def add(self, item):
        newKnapsack = Knapsack(self.items + [item],
            self.totalValue + item.value, 
            self.totalWeight + item.weight)
        newKnapsack.items.sort(key=lambda item: item.name)
        
        return newKnapsack

    def remove(self, item):
        newKnapsack = Knapsack([i for i in self.items if i.name != item.name],
            self.totalValue - item.value,
            self.totalWeight - item.weight)

        return newKnapsack

    def isIn(self, item):
        if len([i for i in self.items if i.name == item.name]) > 0:
            return True
        else:
            return False

    def meetsWeight(self, item, maxWeight):
        if (self.totalWeight + item.weight > maxWeight):
            return False
        else:
            return True

    def print(self):
        print([item.name for item in self.items], "Total Value:", self.totalValue, "| Total Weight:", self.totalWeight)