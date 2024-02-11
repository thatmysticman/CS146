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

The time complexity of the given expression (1 + 1) + 7N is represented in Big O notation as O(N). This shows that the algorithm's time complexity grows linearly with the size of the input (N), with a constant factor (7) influencing the rate of growth. The order of growth for this function is linear.
