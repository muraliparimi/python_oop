# Find smallest missing number
# nodes = [5, 4, 3, 1] , expected 2
# nodes = [3, 2, 1], expected 4


def find_smallest_missing_numer(nums):
    nums_set = set(nums)
    smallest = 1

    while smallest in nums_set:
        smallest += 1
    return smallest



if __name__ == '__main__':
    input1 = 