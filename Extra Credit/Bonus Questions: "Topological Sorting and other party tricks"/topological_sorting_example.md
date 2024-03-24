### Topological Sorting Algorithms: Kahn's Algorithm, BFS, and DFS

#### Example Graph
| Node | Adjacent Nodes |
|------|----------------|
| 0    | 1, 4           |
| 1    | 2, 3           |
| 2    | 5              |
| 3    |                |
| 4    |                |
| 5    |                |

##### Example Explanation
In this adjacency list:
- Node `0` is connected to nodes `1` and `4`.
- Node `1` is connected to nodes `2` and `3`.
- Node `2` is connected to node `5`.
- Node `3` has no outgoing edges.
- Node `4` has no outgoing edges.
- Node `5` has no outgoing edges.

#### Sample Input

`graph = {`    
    `0: [1, 4],`    
    `1: [2, 3],`   
    `2: [5],`    
    `3: [],`   
    `4: [],`    
    `5: []`    
`}`    

##### Kahn's Algorithm
Kahn's algorithm starts by checking the connections of each vertex and then uses a queue to find vertices without incoming connections. Here's how it sorts our example graph:    
`Kahn's Algorithm: [0, 1, 4, 2, 3, 5]`    

##### BFS
Breadth-First Search (BFS) also sorts by checking connections and using a queue. Here's how BFS sorts our example graph:    
`BFS: [0, 1, 4, 2, 3, 5]`    

##### DFS
Depth-First Search (DFS) sorts by exploring paths as far as possible before backtracking. Here's how DFS sorts our example graph:     
`DFS: [0, 4, 1, 3, 2, 5]`     

