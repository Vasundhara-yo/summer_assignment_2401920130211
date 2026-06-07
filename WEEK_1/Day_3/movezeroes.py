class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in nums:
            if j!= 0:
                nums[i]=j
                i+=1

        while(i<len(nums)):
            nums[i] = 0
            i+=1
