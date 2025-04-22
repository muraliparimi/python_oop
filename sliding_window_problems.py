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


# number of subarrays of size k with average greater than given threshold.

class numOfSubarrays:
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
    

# subarray with same number repetition in a given array. find its length.
class LengthySubarray:
    def lengthySubarray(self, arr: List[int]) -> int:
        ans = 1,
        max_len = 1
        L = 0
        R = L + 1
        while L <= R < len(arr):
            if arr[L] == arr[R]:  
                ans += 1
                max_len = max(ans, max_len)
                R += 1
            else:
                L=R
                ans = 1
                R +=1
        return max_len
    
    def longestsubarray(self, arr: List[int]) -> int:
        length = 0
        L = 0
        for R in range(len(arr)):
            if arr[L] != arr[R]:
                L = R
            length = max(length, R - L + 1)
        return length

# Leetcode 



if __name__ == '__main__':
    x = LengthySubarray()
    print(x.lengthySubarray([1,2,2,3,3,3]))
    print(x.longestsubarray([1,2,2,3,3,3]))