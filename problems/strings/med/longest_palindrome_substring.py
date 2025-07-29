"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    result = ""
    for i in range(len(s)):
        # Odd-length palindromes
        temp = expand(i, i)
        if len(temp) > len(result):
            result = temp
        # Even-length palindromes
        temp = expand(i, i + 1)
        if len(temp) > len(result):
            result = temp

    return result

def test_longestPalindrome():
    assert longestPalindrome("babad") in ["bab", "aba"], "Error en caso 'babad'"
    assert longestPalindrome("cbbd") == "bb", "Error en caso 'cbbd'"
    assert longestPalindrome("abcabcbb") in ["a", "b", "c"], "Error en caso 'abcabcbb'"
    assert longestPalindrome("a") == "a", "Error en caso 'a'"
    assert longestPalindrome("ac") in ["a", "c"], "Error en caso 'ac'"
    assert longestPalindrome("racecar") == "racecar", "Error en caso 'racecar'"

    print("Todos los tests pasaron correctamente.")

test_longestPalindrome()