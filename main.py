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

nums = input()
nums=eval(nums)
target = int(input())
print(twoSum(nums, target))

C:\Users\seonahryu\Desktop\swe