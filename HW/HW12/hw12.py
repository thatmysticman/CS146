def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    edges = []

    # Add edges from wells
    for i, cost in enumerate(wells):
        edges.append((cost, 0, i + 1))

    # Add edges from pipes
    for pipe in pipes:
        edges.append((pipe[2], pipe[0], pipe[1]))

    # Sort edges by their cost
    edges.sort()

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    totalCost = 0

    for cost, house1, house2 in edges:
        xRoot = find(parent, house1)
        yRoot = find(parent, house2)

        if xRoot != yRoot:
            union(parent, rank, xRoot, yRoot)
            totalCost += cost

    return totalCost

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xRoot = find(parent, x)
    yRoot = find(parent, y)

    if rank[xRoot] < rank[yRoot]:
        parent[xRoot] = yRoot
    elif rank[xRoot] > rank[yRoot]:
        parent[yRoot] = xRoot
    else:
        parent[yRoot] = xRoot
        rank[xRoot] += 1
