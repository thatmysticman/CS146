def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: (x[0], x[1])) 

    endTimeMinHeap = []

    for interval in intervals:
        if endTimeMinHeap and endTimeMinHeap[0] <= interval[0]:
            heapq.heappop(endTimeMinHeap)
        heapq.heappush(endTimeMinHeap, interval[1])

    return len(endTimeMinHeap)
