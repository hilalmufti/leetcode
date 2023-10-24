from typing import List

"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def is_empty(ss: List[str]) -> bool:
        return len(ss) == 0

def is_open(c: str) -> bool:
    return c == "(" or c == "{" or c == "["

def is_matching(s : str) -> bool:
    return s == "()" or s == "{}" or s == "[]"

class Solution:
    def isValid(self, s: str) -> bool:
        ps: List[str] = []
        for c in s:
            if is_open(c):
                ps.append(c)
            elif is_empty(ps) or not is_matching(ps.pop() + c):
                return False
        return is_empty(ps)