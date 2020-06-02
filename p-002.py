def fibonacci_lim (limit):
    nums = [1,2]

    while nums[len(nums) - 1] < limit:
        nums.append(nums[len(nums)-1] + nums[len(nums)-2])
    nums.pop()
    return nums

#Filter by evens

def answer(n): return sum([x for x in fibonacci_lim(n) if x%2 == 0])


