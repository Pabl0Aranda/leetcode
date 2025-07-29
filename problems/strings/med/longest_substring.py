"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    max_len = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len

def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring("abcabcbb") == 3, "Error en caso 'abcabcbb'"
    assert lengthOfLongestSubstring("bbbbb") == 1, "Error en caso 'bbbbb'"
    assert lengthOfLongestSubstring("pwwkew") == 3, "Error en caso 'pwwkew'"
    assert lengthOfLongestSubstring("") == 0, "Error en caso cadena vacía"
    assert lengthOfLongestSubstring("abcdefg") == 7, "Error en caso sin duplicados"
    assert lengthOfLongestSubstring("abba") == 2, "Error en caso 'abba'"
    print("Todos los tests pasaron correctamente.")

# Tests
test_lengthOfLongestSubstring()
