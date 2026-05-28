# Perfect Sum Problem

## Problem Statement

Given an array `arr[]` of non-negative integers and an integer `sum`, the task is to count all subsets of the given array whose sum is equal to the given `sum`.

---

# Examples

## Example 1

### Input

```text id="g8r4me"
arr[] = [2, 3, 5, 6, 8, 10]
sum = 10
```

### Output

```text id="f2e1qw"
3
```

### Explanation

The subsets having sum `10` are:

* `[2, 3, 5]`
* `[2, 8]`
* `[10]`

---

## Example 2

### Input

```text id="f6m2oz"
arr[] = [1, 2, 3, 3]
sum = 6
```

### Output

```text id="yx81pl"
3
```

### Explanation

The subsets having sum `6` are:

* `[1, 2, 3]`
* `[1, 2, 3]`
* `[3, 3]`

---

## Example 3

### Input

```text id="m3qv0k"
arr[] = [0, 0, 1]
sum = 1
```

### Output

```text id="6n9qca"
4
```

### Explanation

The subsets having sum `1` are:

* `[1]`
* `[0, 1]`
* `[0, 1]`
* `[0, 0, 1]`

---

# Constraints

* `1 ≤ arr.size() ≤ 10^3`
* `0 ≤ arr[i] ≤ 10^3`
* `0 ≤ sum ≤ 10^3`
