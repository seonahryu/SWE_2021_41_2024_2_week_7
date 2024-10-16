from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    ans = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans
    return ans

#Test cases
print(f"Test case 1 Output: {twoSum([2,7,11,15], 9)}")
print(f"Test case 2 Output: {twoSum([3,2,4], 6)}")
print(f"Test case 3 Output: {twoSum([3,3], 6)}")

"""
nums = input()
nums = eval(nums)
target = int(input())
print(twoSum(nums, target))

"""