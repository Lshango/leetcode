# The 5th problem from leetcode, (hard) regular match;
class Pro005Solution(object):
    @classmethod
    def longest_palindrome(cls, s):
        """
        :param s: string
        :return: string
        """
        return s


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
