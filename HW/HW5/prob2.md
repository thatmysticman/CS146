# HW5 - Problem 1

### Pseudocode:
`yetAnotherFunc(n):`     
`  if n > 1:`             //1    
`    for(i=0;i<10n;i++)`  //10n  
`      doSomething;`      //1   
`    yetAnotherFunc(n/2);`//T  
`    yetAnotherFunc(n/2);`//T   

### Recurrence Relation:

`T(n) = 2T(n/2) + 10n`, for `n > 1`

### Solution:

Using Master Theorem "Divide and Conquer Algorithms" - `T(N) = aT(N/b) + f(N)`:   
- a = 2    
- b = 2     
- f(n) = 10n   
- log_b(a) = log_2(2) = 1  
  
Using the 3rd case:   
T(n) = Θ(f(n) * log n)   
T(n) = Θ(10n * log n)   
`T(n) = Θ(n log n)`    
