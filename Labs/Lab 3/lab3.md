#### Problem 1:
Let`s compare some basic math functions to refresh our memory. For each of the following, just write which function is asymptotically greater (So, you should be thinking about your asymptotic notations!). Show your reasoning for the same.

1. 10000000000n^2 vs n^3   
   `Answer: n^3, because the exponent in n^3 is higher than the exponent in 10000000000n^2`
3. n^2 log(n) vs n(log(n))^10   
   `Answer: n^2 log(n), has a higher growth rate than n(log(n))^10`   
5. n^(logn) vs 2^(sqrt(n))  
   `Answer: 2^(sqrt(n)), because the exponential function 2^(sqrt(n)) grows faster than the power function n^(logn)`      
7. 2^n vs 2^2n    
   `Answer: 2^2n, because the exponent in 2^2n is higher than the exponent in 2^n`


#### Problem 2:
Now let`s examine some [pseudo]code and apply asymptotic notation to it. 

`isPrime(n):`   
  `for(i = 2, i*i <= n; i++) {`    
   ` if(n % x == 0) {  `  
      `return false  `  
   ` }     `    
  `return true`

##### Best Case   
`- Occurs when the input number n is 2 or any other prime number.`    
`- Time Complexity: O(1)`   
##### Worst Case    
`- Occurs when n is a large prime number or a prime number that is close to the largest number in the range`    
`- Time Complexity: O(sqrt(n))`   
##### Average Case      
`- On average, a factor will be found in the first half of the loop.`    
`- Time Complexity: O(sqrt(n))`   
