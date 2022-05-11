# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# 123 -> 321, -123 -> -321

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT32 = 1 << 31
        neg = 1
        if x < 0:
            neg = -1
            x *= -1
        rev = 0
        while x:
            popped = x % 10
            x = x//10
            # it will overflow
            if rev > MAX_INT32/10:
                return 0
            rev = rev * 10 + popped
        return neg * rev
