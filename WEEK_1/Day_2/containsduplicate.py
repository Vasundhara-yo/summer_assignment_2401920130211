class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for nums in nums:
            if nums in s:
                return True
            s.add(nums)
        return False   