def searchRange(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            start = end = mid
            while start >0 and nums[start-1] == target:
                start -=1
            while end < len(nums) -1 and nums[end+1] == target:
                end += 1
            return [start, end]
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return [-1, -1]


print(searchRange([1,3,5,6,7,7,7,7,8,9],7))
