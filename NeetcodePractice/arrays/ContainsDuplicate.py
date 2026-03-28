# https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

def hasDuplicate(nums):
        return len(set(nums)) < len(nums)
