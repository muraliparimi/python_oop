# Given an array, return true if there are two elements within a window of size k that are equal.

from typing import List
def closeDuplicates(nums, k):
    window = set() # current window of size <= k.
    L = 0
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        target_sum = threshold * k
        size = len(arr)
        if k > size:
            return ans
        if k == size:
            if sum(arr) >= target_sum:
                ans +=1
                return ans
            else:
                return ans
        window_sum = sum(arr[:k])
        if window_sum >= target_sum:
            ans +=1
        for i in range(k, size):
            window_sum = window_sum + arr[i] - arr[i-k]
            if window_sum >= target_sum:
                ans +=1
        return ans

if __name__ == '__main__':
    print(closeDuplicates([1,2,3,2,3,3], 3))