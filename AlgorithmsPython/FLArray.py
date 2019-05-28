# Find first and last position of the element in the sorted array in log time

class Solution:
    def searchRange(self, nums, target):
        """

        :param nums:List[int]
        :param target: int
        :return: List[int]
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return [self.find_left(nums, 0, mid, target), self.find_right(nums, mid, len(nums) - 1, target)]
        return [-1, 1]

    def find_left(self, nums, left, right, target):
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid - 1] < target:
                return mid
            else:
                right = mid - 1
        return left

    def find_right(self, nums, left, right, target):
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid + 1] > target:
                return mid
            else:
                left = mid + 1
        return right

test=[5,7,7,8,8,10]

print(Solution().searchRange(test,8))