"""
This is for learning algorithm by leetcode.
Author: lshango
Date: 20190905
"""

'''The 1st problem from leetcode, (easy)'''
class Pro001Solution:
    @classmethod
    def two_sum(cls, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        # num_to_index: dictionary from num to index
        num_to_index = {}
        for i, num in enumerate(nums):
            if target-num in num_to_index:
                return [num_to_index[target-num], i]
            num_to_index[num] = i
        return []


'''The 2nd problem from leetcode, (medium)'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Pro002Solution:
    @classmethod
    def add_two_numbers(cls, l1, l2):
        """
        :param l1: listNode
        :param l2: listNode
        :return: listNode
        """
        prev = r_val = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        return r_val.next

'''The 3rd problem from leetcode, (medium)'''
class Pro003Solution:
    @classmethod
    def length_of_longest_substring(cls, s):
        """
        :param s: string
        :return: int
        """
        sub_string = ""
        result = 0
        for i in range(0, len(s)):
            if s[i] in sub_string:
                result = max(result, len(sub_string))
                prev = sub_string.find(s[i])
                sub_string = sub_string[(prev+1):] + s[i]
            else:
                sub_string += s[i]
        return max(result, len(sub_string))

    @staticmethod
    def length_of_longest_substring_1(s):
        """
        :param s: string
        :return: int
        """
        last_seen = {}
        start = 0
        max_length = 0
        for i, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] > start:
                start = last_seen[ch] + 1
            else:
                max_length = max(max_length, i - start + 1)
            last_seen[ch] = i
        return max_length


'''The 4th problem from leetcode, (hard)'''
class Pro004Solution:
    @classmethod
    def find_median_sorted_arrays(cls, nums1, nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: float
        """