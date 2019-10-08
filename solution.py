"""
This is for learning algorithm by leetcode.
Author: lshango
Date: 20190905
"""

# The 1st problem from leetcode, (easy)
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


# The 2nd problem from leetcode, (medium)
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


# The 3rd problem from leetcode, (medium)
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


# The 4th problem from leetcode, (hard)
class Pro004Solution:
    @classmethod
    def find_median_sorted_arrays(cls, nums1, nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: float
        """
        def get_kth_smallest(a_start, b_start, k):
            if k <= 0 or k > len(nums1) - a_start + len(nums2) - b_start:
                raise ValueError("The input value error!")
            if len(nums1) == a_start:
                return nums2[b_start + k - 1]
            if len(nums2) == b_start:
                return nums1[a_start + k - 1]
            if k == 1:
                return min(nums1[a_start], nums2[b_start])

            mid_a, mid_b = float('inf'), float('inf')
            if k//2 <= len(nums1) - a_start:
                mid_a = nums1[a_start + k // 2 - 1]
            if k//2 <= len(nums2) - b_start:
                mid_b = nums2[b_start + k // 2 - 1]

            if mid_a < mid_b:
                return get_kth_smallest(a_start + k // 2, b_start, k - k // 2)
            else:
                return get_kth_smallest(a_start, b_start + k // 2, k - k // 2)

        right = get_kth_smallest(0, 0, 1 + (len(nums1) + len(nums2))//2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return right
        else:
            left = get_kth_smallest(0, 0, (len(nums1) + len(nums2))//2)
            return (left + right)/2.0


# The 6th problem from leetcode, (medium) zigzag;
class Pro006Solution(object):
    @classmethod
    def convert(cls, s, rowNums):
        """
        :param s: string
        :param rowNums: int
        :return: string
        """
        if rowNums == 1:
            return s

        zigzag = [[] for _ in range(rowNums)]
        row = 0
        direction = -1
        for c in s:
            zigzag[row].append(c)
            if row == 0 or row == rowNums - 1:
                direction = -direction
            row += direction
        return "".join([c for _ in zigzag for c in _])
# print(Pro006Solution.convert("LEETCODEISHIRING", 3))


# The 7th problem from leetcode. (easy) reverse the signed int;
class Pro007Solution(object):
    @classmethod
    def reverse(cls, x):
        """
        :param x: int
        :return: int
        """
        neg = x < 0
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x = x // 10
        if result > 2**31 - 1:
            return 0
        return result if not neg else -result
# print(Pro007Solution.reverse(-123))


# The 8th problem from leetcode, (medium) atoi;
class Pro008Solution(object):
    @classmethod
    def my_atoi(cls, s):
        """
        :param s: string
        :return: int
        """
        s = s.strip()
        neg = False
        if s and s[0] == '-':
            neg = True
        if s and (s[0] == '+' or s[0] == '-'):
            s = s[1:]

        digit = {_ for _ in '0123456789'}
        result = 0
        for c in s:
            if c not in digit:
                break
            result = result * 10 + int(c)

        if neg:
            result = -result
        return max(min(result, 2 ** 31 - 1), -2 ** 31)
# print(Pro008Solution.my_atoi('-1234'))


# The 9th problem from leetcode, (easy) isPalindrome;
class Pro009Solution(object):
    @classmethod
    def is_palindrome(cls, x):
        """
        :param x: int
        :return: bool
        """
        str0 = str(x)
        str1 = str0[::-1]
        return str0 == str1


# The 11th problem from leetcode, (medium) maxArea;
class Pro011Solution(object):
    @classmethod
    def max_area(cls, height):
        """
        :param height: list[int]
        :return: int
        """
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = max(area, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


# The 12th problem from leetcode, (medium) intToRoman;
class Pro012Solution(object):
    @classmethod
    def int_to_roman(cls, num):
        """
        :param num: integer
        :return: string
        """
        mapped = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                  100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                  10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        roman = ''
        for i, s in mapped.items():
            while i <= num:
                roman += s
                num -= i
        return roman
# print(Pro012Solution.int_to_roman(1994))


# The 13th problem from leetcode, (medium) romanToInt;
class Pro013Solution(object):
    @classmethod
    def roman_to_int(cls, s):
        """
        :param s: string
        :return: integer
        """
        mapped = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                  100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                  10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        num = 0
        for i, st in mapped.items():
            while s[:len(st)] == st:
                num += i
                s = s[len(st):]
        return num
# print(Pro013Solution.roman_to_int('MCMXCIV'))


# The 14th problem from leetcode, (medium) longestCommonPrefix;
class Pro014Solution(object):
    @classmethod
    def longest_common_prefix(cls, strs):
        """
        :param strs: list[string]
        :return: string
        """
        if not strs:
            return ''

        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
# strs = ['flsse','flseq', 'flsqwrrete']
# print(Pro014Solution.longest_common_prefix(strs))

