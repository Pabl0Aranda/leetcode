"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""

def reverse_integer(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        # Check overflow BEFORE adding the digit
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result

def test_reverse_integer():
    assert reverse_integer(123) == 321
    assert reverse_integer(-123) == -321
    assert reverse_integer(120) == 21
    assert reverse_integer(0) == 0
    assert reverse_integer(1534236469) == 0  # Overflow
    assert reverse_integer(-1563847412) == 0  # Negative Overflow
    print("All test cases passed.")

test_reverse_integer()