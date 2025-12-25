def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None

nums = [2, 7, 11, 15]
print(two_sum(nums, 9))  # (0, 1)
