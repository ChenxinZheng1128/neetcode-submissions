class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to simulate 32-bit integer behavior
        mask = 0xFFFFFFFF
        # Maximum positive integer for a 32-bit system
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # a ^ b calculates the sum without carry
            # (a & b) << 1 calculates the carry
            # We apply the mask to keep everything within 32 bits
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # If 'a' represents a negative number (greater than the 32-bit max positive)
        # we restore it to Python's arbitrary precision negative representation
        return a if a <= max_int else ~(a ^ mask)