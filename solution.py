# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Determines if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers at the head of the list
        slow = head
        fast = head
        
        # Traverse the list as long as the fast pointer can move two steps
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
                
        # If fast reaches the end (None), there is no cycle
        return False
