import math

def main():
    points = {
        'A': [1, 6],
        'B': [1002, 20],
        'C': [498, 651],
        'D': [6, 10],
        'E': [510, 622],
        'F': [503, 632],
        'G': [4, 9],
        'H': [1010, 25],
        'I': [1006, 30],
        'J': [502, 680]
    }
    partitions = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F', 'G'],
        ['H', 'I', 'J']
    ]

    while True:
        centroids = []
        # Find Centroids
        for idx, cluster in enumerate(partitions):
            x, y = [0, 0]
            for p in cluster:
                x += points[p][0]
                y += points[p][1]
            
            centroids.append([x / len(cluster), y / len(cluster)]) 
            print("Cluster:", cluster)
            print("Centroid:", centroids[idx])
        print()

        # Divide Points
        newPartitions = [[], [], []]
        for p, l in points.items():
            minDist = 10000
            minIdx = -1
            #print(p, l)
            for idx, c in enumerate(centroids):
                newDist = distance(l, c)
                #print(c, newDist)
                if newDist < minDist:
                    minDist = newDist
                    minIdx = idx
            newPartitions[minIdx].append(p)
        
        newPartitions = [p for p in newPartitions if p]
        print(newPartitions)

        # Print Cost
        sum = 0
        for idx, cluster in enumerate(partitions):
            for p in cluster:
                sum += distance(points[p], centroids[idx])**2
                print(points[p], distance(points[p], centroids[idx])**2, sum)
        print(sum)
        print()

        if partitions != newPartitions:
            partitions = newPartitions
        else:
            break

def distance(point, centroid):
    x1, y1 = point
    x2, y2 = centroid
    return math.hypot(x2 - x1, y2 - y1)

main()