# Find subarray of size 'k' with maximum sum in a given array



from typing import List
from math import inf
from copy import deepcopy

def max_sum_sub_array(num_array: List[int], k: int) -> List[int]:
    array_len = len(num_array)
    if array_len == k:
        return num_array
    if array_len < k:
        return None
    max_sum= -inf
    #result = []
    result = subarray = num_array[:k]
    #print(f"initial subarray of length {k} is {subarray}")
    initial_sum = sum(subarray)
    max_sum = running_sum = initial_sum
    for i in range(1, array_len-k+1):
        #print(f"running at iteration {i}")
        first_idx_val = subarray.pop(0)
        next_idx_val = num_array[i+k-1]
        subarray.append(next_idx_val)
        running_sum = running_sum - first_idx_val + next_idx_val
        if running_sum > max_sum:
            max_sum = running_sum
            result = deepcopy(subarray[:])
    return result



# if __name__ == '__main__':
#     num_array = [-1, 0, -1, 3, 5, -2, 7, -7, 9, 4, -3, 6]
#     k = 3
#     print(f"subarray with max sum for input {num_array} of length {k} is {max_sum_sub_array(num_array, k)}")

# without creating and manipulating subarray, an efficient approach

def max_sum_sub_array_1(num_array: List[int], k: int) -> List[int]:
    array_len = len(num_array)
    if array_len == k:
        return num_array
    if array_len < k:
        return None
    result = num_array[:k]
    initial_sum = sum(result)
    max_sum = running_sum = initial_sum
    for i in range(1, array_len - k + 1):
        running_sum = running_sum - num_array[i-1] + num_array[i+k-1]
        if running_sum > max_sum:
            max_sum = running_sum
            result = num_array[i:i+k]
    return result

#leetcode #643 implementation
# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        array_len = len(nums)
        if array_len < k:
            return None
        if array_len == k:
            return sum(nums)/k
        max_sum = running_sum = sum(nums[:k])
        for i in range(1, array_len -k +1):
            running_sum = running_sum - nums[i-1] + nums[i+k-1]
            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum/k


# 3. Longest Substring Without Repeating Characters

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set to contain and track uniq characters
        #s = set()
        dq = deque()
        max_len =  running_len = 0
        for i in s:
            if i not in dq:
                #s.add(i)
                dq.append(i)
                running_len +=1
            else:
                if running_len > max_len:
                    max_len = running_len
                idx = dq.index(i)
                while idx >-1:
                    dq.popleft()
                    idx -=1
                dq.append(i)
                running_len = len(dq)
        return running_len if running_len > max_len else max_len
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        # create a set to contain and track uniq characters
        #s = set()
        dq = deque()
        max_len =  running_len = 0
        for i in s:
            if i not in dq:
                #s.add(i)
                dq.append(i)
                running_len +=1
            else:
                if running_len > max_len:
                    max_len = running_len
                #idx = dq.index(i)
                while i in dq:
                    dq.popleft()
                dq.append(i)
                running_len = len(dq)
        return running_len if running_len > max_len else max_len

if __name__ == '__main__':
    num_array = [-1, 0, -1, 3, 5, -2, 7, -7, 9, 4, -3, 6]
    k = 3
    # print(f"subarray with max sum for input {num_array} of length {k} is {max_sum_sub_array(num_array, k)}")
    print(f"subarray with max sum for input {num_array} of length {k} is {max_sum_sub_array_1(num_array, k)}")