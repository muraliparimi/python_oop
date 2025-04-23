
class RotatedArrays:
    def __init__(self, arr):
        self.arr = arr

    def find_min(self):
        pass

    def find_max(self):
        pass

    def find_pivot_index(self):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.arr[mid-1] < self.arr[mid] < self.arr[mid+1]:
                return mid

    def findtarget(self, target):
        left, right = 0, len(self.arr) - 1 
        while left <= right:
            mid = (left + right) // 2

            if self.arr[mid] == target:
                return mid
            
            if self.arr[left] <= self.arr[mid]:
                if self.arr[left] <= target < self.arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if self.arr[mid] < target <= self.arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    


if __name__ == '__main__':
    x = RotatedArrays([4,5,6,7,0,1,2])
    print(x.findtarget(3))

