# Unique Pairs with Sum Zero

## Problem Statement

Given an integer array `arr`, return all the unique pairs `[arr[i], arr[j]]` such that:

* `i != j`
* `arr[i] + arr[j] == 0`

> **Note:**
>
> * The pairs must be returned in sorted order.
> * The solution array should also be sorted.
> * The answer must not contain any duplicate pairs.

---

# Examples

## Example 1

### Input

```text id="j3x8np"
arr = [-1, 0, 1, 2, -1, -4]
```

### Output

```text id="m7q2va"
[[-1, 1]]
```

### Explanation

The pair `[-1, 1]` sums to `0`.

---

## Example 2

### Input

```text id="b5k9zu"
arr = [-2, 2, -1, 1, 3]
```

### Output

```text id="t1f6rw"
[[-2, 2], [-1, 1]]
```

### Explanation

Both pairs sum to `0`.

---

## Example 3

### Input

```text id="v4c7yo"
arr = [1, 2, 3]
```

### Output

```text id="n8p1ld"
[]
```

### Explanation

No pair exists whose sum is `0`.

---

# Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-10^5 ≤ arr[i] ≤ 10^5`
