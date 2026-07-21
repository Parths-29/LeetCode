class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        base_ones = s.count('1')
        t = '1' + s + '1'
        zero_blocks = [len(x) for x in s.split('1') if x]
        if not zero_blocks:
            return base_ones
        if len(zero_blocks) < 2:
            return base_ones 
        max_gain = max(a + b for a, b in zip(zero_blocks, zero_blocks[1:]))
        return base_ones + max_gain


        