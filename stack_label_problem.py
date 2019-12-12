# The 20th problem from leetcode, (easy) isValidParentheses;
class Pro020Solution(object):
    @classmethod
    def is_valid(cls, s):
        """
        :param s: string
        :return: bool
        """
        stack = []
        left_p = '{[('
        right_p = '}])'
        for c in s:
            if c in left_p:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == left_p[right_p.find(c)]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False
# print(Pro020Solution.is_valid('(])'))


# The 42th problem from leetcode, (hard)Trapping Rain Water
class Pro042Solution(object):
    @classmethod
    def trap(cls, height):
        """
        :param height: : List[int]
        :return: int
        """
        pass