class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return True
        stack = []
        slow = head
        fast = head
        current = head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        while mid != None:
            stack.append(mid.val)
            mid = mid.next
        while len(stack) > 0:
            if stack.pop() != current.val:
                return False
            current = current.next
        return True
        