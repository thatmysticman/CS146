    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> endTimeMinHeap = new PriorityQueue<>();

        for (int[] interval : intervals) {
            if (!endTimeMinHeap.isEmpty() && endTimeMinHeap.peek() <= interval[0]) {
                endTimeMinHeap.poll();
            }
            endTimeMinHeap.offer(interval[1]);
        }

        return endTimeMinHeap.size();
    }
