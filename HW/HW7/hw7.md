# HW 7

## Problem
Given an array of time intervals `intervals` where `intervals[i] = [start_i, end_i]`, representing the start and end time for a particular job that needs to be executed, return the minimum number of servers required to run all jobs.

### Constraints:

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`    

## High-Level Approaches

### Python Approach

1. Define a function `minMeetingRooms` with parameters `self`, `intervals: List[List[int]]`, and return type `int`.
2. If `intervals` is empty, return 0 as there are no servers.
3. Sort the `intervals` list based on the start time (`x[0]`), and if start times are equal, then based on the end time (`x[1]`). This is done to have a chronological order of intervals.
4. Create an empty list `endTimeMinHeap` to keep track of the end times of jobs using a min-heap.
5. Iterate through each interval in the sorted `intervals` list.
6. If `endTimeMinHeap` is not empty and the smallest end time in the heap is less than or equal to the start time of the current interval, pop that end time from the heap. This signifies that the job associated with that end time has ended.
7. Push the end time of the current interval to the `endTimeMinHeap`. This signifies that a new server is scheduled.
8. After processing all intervals, return the length of the `endTimeMinHeap`, which represents the minimum number of servers required.

### Java Approach

1. Define a method `minMeetingRooms` that takes a 2D array `int[][] intervals` as input and returns an int.
2. If `intervals` is null or has length 0, return 0 as there are no servers.
3. Sort the `intervals` array based on the start time (`a[0]`). This is done to have a chronological order of intervals.
4. Create a `PriorityQueue<Integer>` named `endTimeMinHeap` to keep track of the end times of jobs using a min-heap.
5. Iterate through each interval in the sorted `intervals` array.
6. If `endTimeMinHeap` is not empty and the smallest end time in the heap is less than or equal to the start time of the current interval, poll that end time from the heap. This signifies that the job associated with that end time has ended.
7. Offer (push) the end time of the current interval to the `endTimeMinHeap`. This signifies that a new job is scheduled.
8. After processing all intervals, return the size of the `endTimeMinHeap`, which represents the minimum number of servers required.
