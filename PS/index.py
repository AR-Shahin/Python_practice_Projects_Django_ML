class Solution(object):
    def maximumProduct(self, nums):
        sum = 1
        nums.sort()
        for i in nums:
            sum *= i
        print(sum)


s = Solution()
s.maximumProduct([-100, -98, -1, 2, 3, 4])
