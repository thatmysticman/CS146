# HW5 - Problem 1

### 1. T(N) = 2T(N-1) + 1
Using Master Theorem "Decreasing Functions" - `T(N) = aT(N-b) + f(n)`:   
- a = 2   
- b = 1   
- f(n) = 1
  
Using the 3rd case:   
T(n) = O(n^(k)a^(n/b)), a = 2, b = 1, k = 0   
T(n) = O(n^(0)2^(n/1))   
`T(n) = O(2^N)`   

### 2. T(N) = 3T(N-1) + n    
Using Master Theorem "Decreasing Functions" - `T(N) = aT(N-b) + f(n)`:   
- a = 3   
- b = 1   
- f(n) = n

Using the 3rd case:   
T(n) = O(n^(k)a^(n/b)), a = 2, b = 1, k = 1   
T(n) = O(n^(1)3^(n/1))   
`T(n) = O(N*3^N)`     

### 3. T(N) = 9T(N/2) + N^2   
Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 9   
- b = 2   
- f(n) = N^2 
- log_b(a) = log_2(9) = 3.17
  
Using the 2nd case:    
T(n) = Θ(N^(log_b(a)) log^(k+1)N)    
T(n) = Θ(N^(log_2(9)) log^(1)N)    
`T(n) = Θ(N^(3.17)log^N)`    

### 4. T(N) = 100T(N/2) + n^(log_2(cn + 1))    
Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 100    
- b = 2     
- f(n) = n^(log_2(cn + 1))   
  
Using the 3rd case:   
Verifying Special Condition a * f(n/b) ≦ c * f(n), c > 1, n > n_0:   
a * f(n/b) = 100 * n^(log_2(c(n/2) + 1))   
c * f(n) = c * n^(log_2(cn + 1))   
   
Hence,   
100 * n^(log_2(c(n/2) + 1)) / (c * n^(log_2(cn + 1))) ≦ 1   
                    100 / c * (cn + 1) / (c(n/2) + 1) ≦ 1   
                                      200 / c(cn + 1) ≦ 1   
                                                  200 ≦ c(cn + 1)   

Assuming 3rd case,   
`T(n) = Θ(f(n)) = Θ(n^(log_2(cn + 1)))`   

### 5. T(N) = 4T(N/2) + (n^(2))(logn)   
Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 4   
- b = 2     
- f(n) = (n^(2))(logn)   
- log_b(a) = log_2(4) = 2   
  
Using the 3rd case:   
Verifying Special Condition a * f(n/b) ≦ c * f(n), c > 1, n > n_0:   
a * f(N/b) = 4 * ((N/2)^(2))(log(N/2)) = 2N^2log(N/2) <=> N * logN   
c * f(N) = c * N^2logN    

Hence,   
N * logN ≦ c * N^2logN   
   2logN ≦ c     

Assuming 3rd case:    
T(n) = Θ(n^(logb(a) + 1))    
T(n) = Θ(n^(2 + 1)) = Θ(n^3)   
`T(n) = Θ(n^3)`   

### 6. T(N) = 5T(N/2) + (n^(2))/(logn)
Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 5   
- b = 2   
- f(n) = (n^(2))/(logn)    
  
Using the 3rd case:   
Verifying Special Condition a * f(n/b) ≦ c * f(n), c > 1, n > n_0:   
a * f(N/b) = 5f(n/2) = 5((n/2)^(2)/log(n/2)) = 5((n/2)^(2)/log(n) - log(2)) < 5n^2/log(n)   
c * f(N) = c * N^2/logN   

Hence,   
5n^2/log(n) ≦ cn^2/log(n)   
          5 ≦ c       
For inequality to hold, c > 5 and n > n_0.   

Assuming 3rd case:      
T(n) = Θ(f(N))   
`T(n) = Θ(N^2/log(N))`   
