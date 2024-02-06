
# HW 2

## Problem
You are given a set of product versions, and there is a function `isBadVersion(version)` that tells you whether a particular version is bad. You need to find the first bad version, which causes all subsequent versions to be bad.

## High-Level Approaches

### Python Approach

1. Set two pointers, `left` and `right`, to the first and last versions.
2. Calculate the middle version `mid` between `left` and `right`.
3. Check if the middle version is a bad version using the `isBadVersion` API.
4. If it is bad, update the `right` pointer to `mid` (inclusive).
5. If it is not bad, update the `left` pointer to `mid + 1`.
6. Repeat the binary search until `left` and `right` pointers meet.
7. Return the value of `left` as the first bad version.

### Java Approach

1. Set two pointers, `left` and `right`, to the first and last versions.
2. Calculate the middle version `mid` between `left` and `right`.
3. Check if the middle version is a bad version using the `isBadVersion` API.
4. If it is bad, update the `right` pointer to `mid` (inclusive).
5. If it is not bad, update the `left` pointer to `mid + 1`.
6. Repeat the binary search until `left` and `right` pointers meet.
7. Return the value of `left` as the first bad version.

### Assumptions

Both approaches assume the existence of the isBadVersion API, which is given externally. The `bool isBadVersion(version)` method returns whether `version` is bad. Without the external API, a placeholder condition is used for testing purposes.
