# Lab 7

## Problem
There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where `edges[i] = [from_i, to_i, weight_i]` represents a bidirectional and weighted edge between cities `from_i` and `to_i`, and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are reachable through some path and whose distance is **at most** `distanceThreshold`, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities **i** and **j** is equal to the sum of the edges' weights along that path.

### Constraints:
- `2 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= from_i < to_i < n`
- `1 <= weight_i, distanceThreshold <= 10^4`
- All pairs `(from_i, to_i)` are distinct.

## High-Level Approaches

### Python Approach

1. Initialize a 2D list `distance` of size `n x n`, where each cell is set to `float('inf')` to represent the distance between cities. Set the diagonal elements to 0 as the distance from a city to itself is 0.
2. Populate the `distance` list using the given `edges`. For each edge `[from_city, to_city, weight]`, set `distance[from_city][to_city] = weight` and `distance[to_city][from_city] = weight` since the edges are bidirectional.
3. Use the Floyd-Warshall algorithm to calculate the shortest distances between all pairs of cities. For each intermediate city `k`, update the distances between cities `i` and `j` if `distance[i][k] + distance[k][j]` is smaller than the current distance `distance[i][j]`.
4. Initialize `min_city` to `-1` and `min_reachable` to `n`.
5. For each city `i`, count the number of reachable cities whose distance is at most `distanceThreshold`. If this count is less than or equal to `min_reachable`, update `min_reachable` and `min_city`.
6. Return `min_city` as the city with the smallest number of reachable cities that satisfy the distance condition.

### Java Approach

1. Initialize a 2D array `distance` of size `n x n`, where each cell is set to `Integer.MAX_VALUE` to represent the distance between cities. Set the diagonal elements to `0` as the distance from a city to itself is `0`.
2. Populate the `distance` array using the given `edges`. For each edge `[from_city, to_city, weight]`, set `distance[from][to] = weight` and `distance[to][from] = weight` since the edges are bidirectional.
3. Use the Floyd-Warshall algorithm to calculate the shortest distances between all pairs of cities. For each intermediate city `k`, update the distances between cities `i` and `j` if both `distance[i][k]` and `distance[k][j]` are not `Integer.MAX_VALUE` and `distance[i][k] + distance[k][j]` is smaller than the current distance `distance[i][j]`.
4. Initialize `minCity` to `-1` and `minReachable` to `n`.
5. For each city `i`, count the number of reachable cities whose distance is at most `distanceThreshold`. If this count is less than or equal to `minReachable`, update `minReachable` and `minCity`.
6. Return `minCity` as the city with the smallest number of reachable cities that satisfy the distance condition.
