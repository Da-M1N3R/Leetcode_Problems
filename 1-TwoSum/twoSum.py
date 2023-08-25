from typing import List
# later add time of execution code
# later add explanation comment
# add time complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[n] = i

# Creating an instance of 'Solution' class
solution = Solution()

# Test case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1)) # Expected: [0, 1]

# Test case 2: Target is not achievable
nums2 = [3, 4, 5, 6]
target2 = 20
print(solution.twoSum(nums2, target2))  # Expected: []
