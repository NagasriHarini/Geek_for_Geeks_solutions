# Minimum Platforms

## Problem Statement

Given arrival `arr[]` and departure `dep[]` times of trains on the same day, find the minimum number of platforms needed so that no train waits.

A platform cannot serve two trains at the same time. If a train arrives before another departs, an extra platform is needed.

**Note:** Time intervals are in the 24-hour format (`HHMM`), where the first two characters represent the hour (`00` to `23`) and the last two characters represent the minutes (`00` to `59`). Leading zeros for hours less than 10 are optional (e.g., `0900` is the same as `900`).

## Examples

### Example 1

Input:

```text
arr[] = [900, 940, 950, 1100, 1500, 1800]
dep[] = [910, 1200, 1120, 1130, 1900, 2000]
```

Output:

```text
3
```

Explanation:

There are at most 3 trains at the station simultaneously, so 3 platforms are required.

### Example 2

Input:

```text
arr[] = [900, 1235, 1100]
dep[] = [1000, 1240, 1200]
```

Output:

```text
1
```

Explanation:

No two trains overlap, so only one platform is needed.

### Example 3

Input:

```text
arr[] = [1000, 935, 1100]
dep[] = [1200, 1240, 1130]
```

Output:

```text
3
```

## Constraints

```text
1 ≤ number of trains ≤ 50000
0000 ≤ arr[i] ≤ dep[i] ≤ 2359
```
