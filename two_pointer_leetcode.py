
# palindrome with two pointer approach

from typing import List


class TwoPointer():

    def is_palindrome(self, input: str) -> bool:
        start = 0
        end = len(input) - 1
        while start < end:
            if input[start] != input[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers)-1
    while start < end:
        sum2 = numbers[start] + numbers[end]
        if sum2 == target:
            return [start+1, end+1]
        elif sum2 < target: # type: ignore
            start +=1
        else:
            end -=1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)): # type: ignore
        # Skip duplicates
        if i>0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1 # starting on next immediate round
        k = len(nums) -1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total> 0:
                k -=1
            elif total < 0:
                j +=1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j +=1
                while nums[j] == nums[j-1] and j<k:
                    j +=1
    return res

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1 
        diff = 0
        area = 0
        while i < j:
            distance = j - i
            height_diff = min(height[i], height[j])
            area = max(area, diff*height_diff)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area








if __name__ == '__main__':
    c = TwoPointer()
    print(c.is_palindrome('abcdcba'))
    print(c.is_palindrome('abcdcba'))
