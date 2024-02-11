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
∴ (1 + 1) + 7N = O(n)

#### Big-Ω Analysis
1N ≤ (1 + 1) + 7N
N ≤ (1 + 1) + 7N, ∀ n ≥ 1
∴ (1 + 1) + 7N = Ω(n)

#### Big-Θ Analysis
1N ≤ (1 + 1) + 7N ≤ 1N + 7N
N ≤ (1 + 1) + 7N ≤ 8N
∴ (1 + 1) + 7N = Θ(n)
