#Two sum
numbers = [2,7,11,15]
target_goal = 9

def twosum(nums,target):
    seen = {}

    for index, num in enumerate(nums):
        other = target - num
        if other in seen:
            return [seen[other], index]
        else:
            seen[num] = index
    return []

result = twosum(numbers, target_goal)
print(result)
