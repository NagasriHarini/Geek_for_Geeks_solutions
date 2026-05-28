# Maximum Subarray Sum

## Problem Statement

You are given an integer array `arr[]`. You need to find the maximum sum of a subarray (containing at least one element) in the array `arr[]`.

> **Note:** A subarray is a continuous part of an array.

---

# Examples

## Example 1

### Input

```text
arr[] = [2, 3, -8, 7, -1, 2, 3]
```

### Output

```text
11
```

### Explanation

The subarray `[7, -1, 2, 3]` has the largest sum `11`.

---

## Example 2

### Input

```text
arr[] = [-2, -4]
```

### Output

```text
-2
```

### Explanation

The subarray `[-2]` has the largest sum `-2`.

---

## Example 3

### Input

```text
arr[] = [5, 4, 1, 7, 8]
```

### Output

```text
25
```

### Explanation

The subarray `[5, 4, 1, 7, 8]` has the largest sum `25`.

---

# Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-10^4 ≤ arr[i] ≤ 10^4`
