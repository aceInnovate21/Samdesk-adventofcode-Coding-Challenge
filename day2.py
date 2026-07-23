def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def is_safe_dampened(levels):
    return is_safe(levels) or any(
        is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels))
    )

with open('input.txt') as f:
    reports = [list(map(int, line.split())) for line in f if line.strip()]

print("Part 1:", sum(is_safe(r) for r in reports))
print("Part 2:", sum(is_safe_dampened(r) for r in reports))


# Solution
# Part 1: 534
# Part 2: 577