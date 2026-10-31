# Linked-Cycle
Python solution for LeetCode 141: Linked List Cycle using Floyd's Tortoise and Hare (Two-Pointer) algorithm with O(n) time and O(1) space complexity.
# LeetCode 141. Linked List Cycle

## Problem Link
[LeetCode 141 - Linked List Cycle](https://leetcode.com)

## Difficulty
Easy

## Approach: Floyd's Cycle Finding Algorithm (Two Pointers)
We use two pointers, `slow` and `fast`, both starting at the head of the linked list. 
* The `slow` pointer moves **1 step** at a time.
* The `fast` pointer moves **2 steps** at a time.

If a cycle exists, the fast pointer will eventually catch up to and meet the slow pointer (`slow == fast`). If the fast pointer reaches the end of the list (`None`), then no cycle exists.

## Complexity Analysis
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list.
- **Space Complexity:** $O(1)$ because we only use two additional pointers, satisfying the constant extra space constraint.

