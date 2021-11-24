

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        l = len(nums)
        list = []
        for i in range(0, l + 1):
            list.append(i)

        for i in range(0, len(list)):
            if not self.binary_search(nums, list[i]):
                return list[i]

    # def linear_search(self, arr, num):
    #     for i in range(0, len(arr)):
    #         if arr[i] == num:
    #             return True
    #     return False

    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1

            # means x is present at mid
            else:
                return True

        # If we reach here, then the element was not present
        return False


s = Solution()
s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
