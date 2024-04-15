def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    distance = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0

    for from_city, to_city, weight in edges:
        distance[from_city][to_city] = weight
        distance[to_city][from_city] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    min_city = -1
    min_reachable = n

    for i in range(n):
        reachable = sum(1 for j in range(n) if i != j and distance[i][j] <= distanceThreshold)
        if reachable <= min_reachable:
            min_reachable = reachable
            min_city = i

    return min_city
