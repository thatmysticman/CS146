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

The time complexity of the given expression 1 + 1 + 1 + 1 + (N+1) + (N)(N+1) + (N)(N+1) + (N)(N) + N is represented in Big O notation as O(N^2). This shows that the algorithm's time complexity grows quadratically with the size of the input (N^2), with a constant factor (4) influencing the rate of growth. The order of growth for this function is quadratic.
