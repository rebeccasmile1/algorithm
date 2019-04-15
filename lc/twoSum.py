class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    return result
    #有序字典也可以
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        temp=dict(zip(range(0,len(nums)),nums))
        result=[]
        for item in temp:
            if (target-temp[item]) in temp.values():
                result.append(item,(target-temp[item]))