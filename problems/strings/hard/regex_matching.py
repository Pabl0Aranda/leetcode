"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    # dp[i][j] = True si s[:i] hace match con p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty string matches empty pattern

    # Manejar patrones como a*, a*b*, a*b*c* que pueden coincidir con cadena vacía
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # El último caracter coincide, heredo el estado anterior
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' puede representar cero del elemento previo
                dp[i][j] = dp[i][j - 2]  # cero ocurrencias

                # o puede representar una o más ocurrencias, si el anterior coincide con s[i-1]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False

    return dp[m][n]

print(isMatch("aa", "a"))       # False
print(isMatch("aa", "a*"))      # True
print(isMatch("ab", ".*"))      # True
print(isMatch("aab", "c*a*b"))  # True
print(isMatch("mississippi", "mis*is*p*."))  # False
