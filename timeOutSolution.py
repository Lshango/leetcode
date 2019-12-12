# The 15th problem from leetcode, (medium) threeSum;
class Pro015Solution(object):
    @classmethod
    def three_sum_timeout(cls, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        nums.sort()
        result = []
        set_ = {" "}
        for left in range(len(nums)):
            for medium in range(left + 1, len(nums)):
                sum = nums[left] + nums[medium]
                r_num = 0 - sum
                string = str(nums[left]) + str(nums[medium]) + str(r_num)
                if string not in set_ and r_num in nums[medium+1:]:
                    set_.add(string)
                    result.append([nums[left], nums[medium], r_num])
        return result

    @classmethod
    def three_sum(cls, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        nums.sort()
        result = []

        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
                elif sums > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


print(Pro015Solution.three_sum([-1, 0, 1, 2, -1, -4]))