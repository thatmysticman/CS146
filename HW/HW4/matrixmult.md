# Matrix Multiplication

## Pseudocode

MATRIX_MULTIPLY(A, B):                                           `1 time`   
  if columns(A) ≠ rows(B):                                       `1 time`   
    raise ValueError("Matrix multiplication is not defined.")    `1 time`   

  rows_A ← number of rows in A                                   `1 time`   
  cols_A ← number of columns in A                                `1 time`   
  cols_B ← number of columns in B                                `1 time`   
  result ← matrix of size rows_A x cols_B filled with zeros      `1 time`   

  for i from 1 to rows_A do:                                     `N + 1 times`   
    for j from 1 to cols_B do:                                   `(N)(N + 1) times`   
    sum ← 0                                                      `(N)(N) times`   
    for k from 1 to cols_A do:                                   `(N)(N + 1) times`   
      sum ← sum + A[i][k] * B[k][j]                              `(N)(N) times`   
    result[i][j] ← sum return result                             `N times`   
  
### Time Complexity

#### Big-O Analysis    
1 + 1 + 1 + 1 + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N ≤ 1N + 1N + 1N + 1N + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N    
4 + 3N + 3N^2 ≤ 4N + 3N + 1 + 3N^2 + N   
4 + 3N + 3N^2 ≤ 4N + 4N + + 1 + 3N^2   
    4 + 4N + 3N^2 ≤ 8N + 3N^2 + 1, ∀ n ≥ 1      
  ∴ 4 + 4N + 3N^2 = O(N^2)     

#### Big-Ω Analysis    
1N + 1N + 1N + 1N + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N ≤ 1 + 1 + 1 + 1 + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N   
4N + 3N + 1 + 3N^2 + N  ≤ 4 + 4N + 3N^2
   4N + 4N + + 1 + 3N^2 ≤ 4 + 4N + 3N^2
          8N + 3N^2 + 1 ≤ 4 + 4N + 3N^2
                    N^2 ≤ 4 + 4N + 3N^2
        ∴ 4 + 4N + 3N^2 = Ω(N^2)     

#### Big-Θ Analysis
N^2 ≤ 1 + 1 + 1 + 1 + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N ≤ 1N + 1N + 1N + 1N + (N + 1) + (N)(N + 1) + (N)(N + 1) + (N)(N) + N   
N^2 ≤ 4 + 4N + 3N^2 ≤ 8N + 3N^2 + 1 
∴ 4 + 4N + 3N^2 = Θ(N^2)   

### Best, Average, Worst Case   

#### Best Case   
- The best-case scenario occurs when the matrices are incompatible, i.e., when the number of columns in matrix A is not equal to the number of rows in matrix B.    
- The time complexity in the best case is constant, hence the time complexity is O(1).    
##### Example     
Input Matrix:     
`A: 2x3 matrix`     
`B: 4x5 matrix`    
- In this case, the matrices are incompatible for multiplication, and the algorithm raises a ValueError.   

#### Average Case    
- The average case depends on the distribution of input matrices.   
- On average, the time complexity can be estimated as O(N^2), where N is the size of the matrices.   
##### Example      
Input Matrix:   
`A: 2x2 matrix`   
`B: 2x2 matrix`   
- In this case, the algorithm will perform two nested loops, resulting in a time complexity of O(N^2).   

#### Worst Case    
- The worst-case scenario occurs when the matrices are compatible for multiplication.   
- The time complexity in the worst case is O(N^2).   
##### Example     
Input Matrix:   
`A: 2x2 matrix`   
`B: 2x2 matrix`   
- Just like the average case, the algorithm will perform two nested loops, resulting in a time complexity of O(N^2).   
