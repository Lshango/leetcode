# The 5th problem from leetcode, (hard) regular match;
class Pro005Solution(object):
    @classmethod
    def longest_palindrome(cls, s):
        """
        :param s: string
        :return: string
        """
        return s

    @classmethod
    def longest_palin(cls, s):
        """
        :param s: string
        :return: string
        """
        def center_expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = end = 0
        for i in range(len(s)):
            len1 = center_expand(i, i)                   # the length is odd，aba
            len2 = center_expand(i, i + 1)               # the length is dou，abba
            maxlen = max(len1, len2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        return s[start: end + 1]

print(Pro005Solution.longest_palin("gphyvqruxjmwhonjjr"))


# The 10th problem from leetcode, (hard) regular match;
class Pro010Solution(object):
    @classmethod
    def is_match(cls, st, rg):
        """
        :param st: string
        :param rg: regular string
        :return: bool
        """
        matched = [[False for _ in range(len(rg) + 1)] for _ in range(len(st) + 1)]
        matched[0][0] = True

        for i in range(len(st) + 1):
            for j in range(1, len(rg) + 1):
                pattern = rg[j - 1]

                if pattern == '.':
                    matched[i][j] = (i != 0 and matched[i-1][j-1])
                elif pattern == '*':
                    star = rg[j-2]
                    matched[i][j] = matched[i][j-2] or (i > 0 and matched[i-1][j] and (star == st[i-1] or star == '.'))
                else:
                    matched[i][j] = (i != 0 and matched[i-1][j-1] and pattern == st[i-1])
        return matched[-1][-1]
# print(Pro010Solution.is_match('abccdf','a.c*.*'))
