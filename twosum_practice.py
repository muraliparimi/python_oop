def twosumpractice_unsorted(nums, target):
    visited = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            return [idx, visited[complement]]
        visited[num] = idx
    return []

def twosumpractice_unsorted_all_matches(nums, target):
    visited = {}
    result = []
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            result.append([idx, visited[complement]])
        visited[num] = idx
    return result


print(twosumpractice_unsorted([1,4,5,7,6,3,2,9], 17))
print(twosumpractice_unsorted([1,4,5,7,6,3,2,9], 16))
print(twosumpractice_unsorted([1,4,5,7,6,3,2,9], 12))
print(twosumpractice_unsorted_all_matches([1,4,5,7,6,3,2,9], 12))
print(twosumpractice_unsorted_all_matches([1,5,4,2,3], 6))