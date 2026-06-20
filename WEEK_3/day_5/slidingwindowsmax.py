from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # check if we have a valid window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


        