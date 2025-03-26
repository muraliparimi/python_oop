"""
 Deque is a good tool to solve problems related to 
 1. Sliding window
 2. Fixed-size recent history
 3. Streams and real-time systems
 4. LRU cache like behavior


# Sliding window maximum

# You've given a stream of integers and fixed window size k. For each window, return the maximum value

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

expected output : [3, 3, 5, 5, 6, 7]

"""
from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def sliding_window_max(nums, k):
    if not nums or k == 0:
        return []
    
    result = []
    window = deque() # to store indices, not values

    for i in range(len(nums)):
        if window[0] <= i - k:
            window.popleft()
        # 2. Remove indices whose values are smaller than nums[i]
        while window and nums[i] > nums[window[-1]]:
            window.pop()

        # Append current index
        window.append(i)

        # 4. Add the max (nums[window[0]]) to result once the first window is done
        if i >= k - 1:
            result.append(nums[window[0]])
    return result