# Insertion Sort Algorithm

## Pseudocode

function insertionSort(arr: Array)        `1 time`   
    for i from 1 to length(arr) - 1       `N + 1 times`   
        key = arr[i]                      `N times`   
        j = i - 1                         `N times`   
        while j >= 0 and arr[j] > key     `N times`   
            arr[j + 1] = arr[j]           `N times`   
            j = j - 1                     `N times`   
        end while   
        arr[j + 1] = key                  `N times`   
    end for   
end function   

### Time Complexity

#### Big-O Analysis   
(1 + 1) + 7N ≤ 1N + 7N   
(1 + 1) + 7N ≤ 8N, ∀ n ≥ 1   
∴ (1 + 1) + 7N = O(N)   

#### Big-Ω Analysis   
1N ≤ (1 + 1) + 7N   
N ≤ (1 + 1) + 7N, ∀ n ≥ 1   
∴ (1 + 1) + 7N = Ω(N)   

#### Big-Θ Analysis   
1N ≤ (1 + 1) + 7N ≤ 1N + 7N   
N ≤ (1 + 1) + 7N ≤ 8N   
∴ (1 + 1) + 7N = Θ(N)   

### Best, Average, Worst Case   

#### Best Case   
- The best-case scenario occurs when the input array is already sorted.   
- The time complexity is O(N), where N is the length of the array.   
##### Example    
Input Array: `[1, 2, 3, 4, 5]`   
- In this case, the outer loop runs N times, and for each iteration of the outer loop, the inner while loop doesn't perform any swaps. Hence, the time complexity is O(N).   

#### Average Case   
- The average-case time complexity is O(N^2).   
- On average, half of the inner loop comparisons result in swaps.   
##### Example    
Input Array: `[5, 2, 1, 4, 3]`   
- In this case, the average number of comparisons and swaps increases, leading to an O(N^2) time complexity.   

#### Worst Case   
- The worst-case scenario occurs when the input array is sorted in reverse order.   
- The time complexity is O(N^2).   
##### Example   
Input Array: `[5, 4, 3, 2, 1]`   
- In this case, for each element in the unsorted array, the inner while loop performs the maximum number of comparisons and swaps, resulting in an O(N^2) time complexity.


