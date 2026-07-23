# Samdesk-adventofcode-Coding-Challenge
Python solutions to Advent of Code 2024 puzzles. Each day's problem is solved in a standalone script with its input file.
## The Problem
 
The engineers at the Red-Nosed reactor need help analyzing safety data. Each line of the input is a **report** — a list of numbers called **levels**.
 
A report is considered **safe** if both conditions hold:
 
1. The levels are either **all increasing** or **all decreasing**
2. Any two adjacent levels differ by **at least 1 and at most 3**
### Example
 
```
7 6 4 2 1    → Safe    (decreasing by 1 or 2)
1 2 7 8 9    → Unsafe  (2 → 7 jumps by 5)
9 7 6 2 1    → Unsafe  (6 → 2 drops by 4)
1 3 2 4 5    → Unsafe  (increases, then decreases)
8 6 4 4 1    → Unsafe  (4 → 4 is neither)
1 3 6 7 9    → Safe    (increasing by 1, 2, or 3)
```
 
**Part 1:** How many reports are safe?
 
**Part 2:** The Problem Dampener allows **one** bad level to be removed. How many reports are safe now?
 
---
 
## The Approach
 
### Part 1 — Difference Array
 
Rather than checking direction and step size separately, the solution computes the **consecutive differences** between adjacent levels:
 
```python
diffs = [b - a for a, b in zip(levels, levels[1:])]
```
 
Both rules then collapse into a single range check:
 
- **All increasing and valid** → every diff falls in `[1, 3]`
- **All decreasing and valid** → every diff falls in `[-3, -1]`
The key insight: because **zero is excluded from both ranges**, equal adjacent values (like `4 4`) fail automatically. No separate check is needed.
 
```python
def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)
```
 
### Part 2 — Brute Force Removal
 
The Problem Dampener tolerates one bad level. Rather than reasoning about *which* level to remove — which gets subtle fast around edge cases — the solution simply tries removing each one:
 
```python
def is_safe_dampened(levels):
    return is_safe(levels) or any(
        is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels))
    )
```
 
**Why brute force is the right call here:** reports contain only 5–8 levels, so at most 8 re-checks per report. With ~1000 reports, that's under 10,000 trivial operations. An "optimized" single-pass solution would be harder to reason about and no faster in practice.
 
The short-circuit on `is_safe(levels)` means already-safe reports skip the removal loop entirely.
 
---
 
## Complexity
 
|        | Time             | Space |
| ------ | ---------------- | ----- |
| Part 1 | O(n) per report  | O(n)  |
| Part 2 | O(n²) per report | O(n)  |
 
Where `n` is the number of levels in a report (small, bounded).
 
---
 
## Running It
 
```bash
python day2.py
```
 
Expects `input.txt` in the same directory.
 
```
Part 1: 534
Part 2: 577
```
