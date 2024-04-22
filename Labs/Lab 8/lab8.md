# Lab 8

## Problem
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

### Constraints:
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## High-Level Approaches

### Python Approach

1. Initialize a dynamic programming (DP) list `dp` of size `amount + 1`, where each element is set to `amount + 1`. This represents the minimum number of coins required to make up the corresponding amount.
2. Set `dp[0] = 0` since it takes 0 coins to make up an amount of 0.
3. Loop through each amount from 1 to `amount`:     
   a. For each amount `i`, loop through each coin denomination in `coins`.    
   b. If the coin denomination `coin` is less than or equal to `i`:
     - Update `dp[i]` to be the minimum of its current value and `dp[i - coin] + 1`. Here, `dp[i - coin] + 1` represents the minimum number of coins required to make up the amount `i` using the current coin denomination `coin`.
4. Return `dp[amount]` if it is less than or equal to `amount`, otherwise return `-1`.

### Java Approach

1. Initialize an integer array `dp` of size `amount + 1`, where each element is set to `amount + 1`. This represents the minimum number of coins required to make up the corresponding amount.
2. Set `dp[0] = 0` since it takes 0 coins to make up an amount of 0.
3. Loop through each amount from `1` to `amount`:     
   a. For each amount `i`, loop through each coin denomination in `coins`.     
   b. If the coin denomination `coin` is less than or equal to `i`:
     - Update `dp[i]` to be the minimum of its current value and `dp[i - coin] + 1`. Here, `dp[i - coin] + 1` represents the minimum number of coins required to make up the amount `i` using the current coin denomination `coin`.
4. Return `dp[amount]` if it is less than or equal to `amount`, otherwise return `-1`.
