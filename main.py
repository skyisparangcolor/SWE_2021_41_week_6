from typing import List 
def twoSum(nums: List[int], target: int): 
    for i in range (0, len(nums)): 
        for j in range (i+1, len(nums)): 
            if nums[i] + nums[j] == target: 
                return [i,j]

nums = list(map(int, input("num = ").split(',')))
target = int(input("target = "))

twoSum(nums, target)
