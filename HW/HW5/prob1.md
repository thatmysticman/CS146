# HW5 - Problem 1

### 1. T(N) = 2T(N-1) + 1
Solving the Recurrence Algebraically (Iteration):    
- Base Case: T(1) = 1     
- Applying Recurrence:    
T(2) = 2 * T(1) + 1 = 2 * 1 + 1 = 3       
T(3) = 2 * T(2) + 1 = 2 * 3 + 1 = 7        
T(4) = 2 * T(3) + 1 = 2 * 7 + 1 = 15        

Based on the pattern, the values of T(N) are doubling with each increase in N.   
For example, T(3) is twice the value of T(2), and T(4) is twice the value of T(3).   
Hence, the growth rate of `T(n) = O(2^N)`.    

Using Master Theorem "Decreasing Functions" - `T(N) = aT(N-b) + f(n)`:   
- a = 2   
- b = 1   
- f(n) = 1
  
Using the 3rd case:   
T(n) = O(n^(k)a^(n/b)), a = 2, b = 1, k = 0   
T(n) = O(n^(0)2^(n/1))   
`T(n) = O(2^N)`   

### 2. T(N) = 3T(N-1) + n    
Solving the Recurrence Algebraically (Iteration):     
- Base Case: T(1) = 1    
- Applying Recurrence:    
T(2) = 3 * T(1) + 2 = 5     
T(3) = 3 * T(2) + 3 = 18      
T(4) = 3 * T(3) + 4	= 58       
 
Based on the pattern, the values of T(N) grow rapidly as N increases due to the exponential term in the recurrence relation, 3^N.    
Hence, the growth rate of `T(N) = O(N*3^N)`.    

Using Master Theorem "Decreasing Functions" - `T(N) = aT(N-b) + f(n)`:   
- a = 3   
- b = 1   
- f(n) = n

Using the 3rd case:   
T(n) = O(n^(k)a^(n/b)), a = 2, b = 1, k = 1   
T(n) = O(n^(1)3^(n/1))   
`T(n) = O(N*3^N)`     

### 3. T(N) = 9T(N/2) + N^2   
Solving the Recurrence Algebraically (Induction):  
- Guess Solution: T(N) ≈ a * N^b * 2^c, where where a, b, and c are constants to be determined
- Induction:
Assume N = k,
T(k) = a * k^b * 2^c
T(2k) = 9T(2k/2) + (2k)^2
T(2k) = 9 * a * (k/2)^b * 2^c + 4k^2
T(2k) = 9a * k^b * 2^(c-1) + 4k^2
- Solving for Constants:
a * 2^c = 9a * 2^(c-1)
      c = 2

a * k^b = 9a * k^b * 2^(-1) + 4k^2
   8k^2 = 0
      k = 0

Since k is a valid input size, the case isn't helpful.
So, since c = 2:
T(N) ≈ a * N^b * 2^(c+1) = a * N^b * 4
a * N^b * 4 = 9 * a * (N/2)^b * 4 + N^2
        N^b = N^b + N^2
          b = 2

Finally,
T(N) ≈ a * N^2 * 4
T(N) = (1/4) * N^2 * 4
`T(N) = O(N^2)`

Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 9   
- b = 2   
- f(n) = N^2 
- log_b(a) = log_2(9) = 3.17
  
Using the 2nd case:    
T(n) = Θ(N^(log_b(a)) log^(k+1)N)    
T(n) = Θ(N^(log_2(9)) log^(1)N)    
`T(n) = Θ(N^(3.17)log^N)`

The Master Theorem leads to looser bounds compared to the direct algebraic analysis I did, solving the recurrence algebraically reveals a tighter bound of T(N) = O(N^2)

### 4. T(N) = 100T(N/2) + n^(log_2(cn + 1))    
Solving the Recurrence Algebraically (Iteration):     
- Base Case: T(1) = c1    
- Applying Recurrence:    
T(N/2) = 100T(N/4) + ((N/2)^(log_2(c(N/2) + 1)))    
T(N/4) = 100T(N/8) + ((N/4)^(log_2(c(N/4) + 1))) 
T(N/8) = 100T(N/16) + ((N/8)^(log_2(c(N/8) + 1)))

For large N, the dominant term in each iteration is the one with the highest exponent, which points to an overall complexity related to `T(n) = Θ(n^(log_2(cn + 1)))`.

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
Solving the Recurrence Algebraically (Iteration):      
T(N) = 4T(N/2) + N^2 log N   
T(N) = 4(4T(N/4) + (N/2)^2 log(N/2)) + N^2 log N   
T(N) = 16T(N/4) + 4N^2 log(N/2) + N^2 log N   
Based on the pattern, N^2 is multiplied by different logarithmic terms.   

Using log(a^b) = b * log(a) to combine logs:    
T(N) = 16T(N/4) + 4N^2(log(N) - log(2)) + N^2 log N    
T(N) = 16T(N/4) + 4N^2 log N - 4N^2 log(2)    

As N grows, the N^2 terms will always outpace the constant terms 4N^2 log(2).    
Therefore, the time complexity of the recurrence is `Θ(N^2 * log N)`.     

Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 4   
- b = 2     
- f(n) = (n^(2))(logn)   
- log_b(a) = log_2(4) = 2 >= 1      
- log^k(N) = log^1(N) = 1      
  
Using the 2nd case:   
T(N) = Θ(N^(log_b(a)) * f(N))     
T(N) = Θ(N^2 * N^2 * logN)      
`T(N) = Θ(N^2 * logN)`      

### 6. T(N) = 5T(N/2) + (n^(2))/(logn)
Solving the Recurrence Algebraically (Iteration):     
- Base Case: T(1) = 1    
- Applying Recurrence:     
T(2) = (2^2)/log(2) + 5 * T(1) = 4/log(2) + 5 * 1 ≈ 7.64     
T(4) = (4^2)/log(4) + 5 * T(2) = 16/2*log(2) + 5 * 7.64 ≈ 78.51     
T(8) = (8^2)/log(8) + 5 * T(4) = 64/3*log(2) + 5 * 78.51 ≈ 986.44      

The values of T(N) grow rapidly due to the dominant term (N^2)/log(N).
The behavior of the recurrence confirms the dominant (N^2)/log(N) term, leading to a complexity of `T(N) = O(N^2/log(N))`.

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
