# Lab 6

## Problem
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Constraints:
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- All the pairs prerequisites[i] are **unique**.

## High-Level Approaches

### Python Approach

1. Initialize an empty dictionary `graph` to represent the courses and their prerequisites.
2. Iterate through each pair `[course, prereq]` in the `prerequisites` list.
3. Add each course as a key in the `graph` dictionary and append its corresponding prerequisite to the list of prerequisites.
4. Implement a depth-first search (DFS) function (`dfs`) to check if it's possible to finish all courses.
5. In the `dfs` function, mark the current course as visited by setting its value to `-1` in the `visited` array.
6. Explore each neighbor of the current course in the `graph`.
7. If any neighbor is already being visited (marked as `-1`), it indicates a cycle, so return `False`.
8. Otherwise, recursively call `dfs` for each neighbor.
9. After exploring all neighbors, mark the current course as visited by setting its value to `1` in the `visited` array.
10. Finally, iterate through all courses and check if each course can be completed by calling the `dfs` function.
11. If any course cannot be completed, return `False`; otherwise, return `True`.

### Java Approach

1. Create a `HashMap` named `graph` to store courses and their prerequisites.
2. Iterate through each pair `[course, prereq]` in the `prerequisites` array.
3. Add each course as a key in the `graph` map and append its corresponding prerequisite to the list of prerequisites.
4. Use an array `visited` to keep track of the visited status of each course during DFS traversal.
5. Implement a DFS function (`dfs`) to check if it's possible to finish all courses.
6. In the `dfs` function, mark the current course as visited by setting its value to `-1` in the `visited` array.
7. If the current course has neighbors (prerequisites), recursively call `dfs` for each neighbor.
8. If any neighbor cannot be completed (cycle detected), return `False`.
9. After exploring all neighbors, mark the current course as visited by setting its value to `1` in the `visited` array.
10. Finally, iterate through all courses and check if each course can be completed by calling the `dfs` function.
11. If any course cannot be completed, return `False`; otherwise, return `True`.
