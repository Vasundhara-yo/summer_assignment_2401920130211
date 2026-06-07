def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                ans[i] = left_sq
                left += 1
            else:
                ans[i] = right_sq
                right -= 1

        return ans
