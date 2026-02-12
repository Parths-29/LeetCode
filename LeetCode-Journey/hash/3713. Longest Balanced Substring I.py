'''
Intuition
Imagine you are at a party where every guest must bring the exact same number of snacks to get in. If one person brings three chips and another brings two, it is not a balanced party. Our job is simply to find the biggest group of characters where everyone has "brought the same number of snacks." Instead of counting everything from scratch each time, we just keep a running tally as we invite more characters into our window.
Approach
We can stroll through the string with a flexible window. We pick a starting character and then stretch the window to the right, one step at a time. As we add new characters, we update a small dictionary (our hash map) to keep count.
The clever part is how we check if the window is balanced. Instead of scanning the whole dictionary every time, we use a neat math trick: if the total length of our substring equals the number of unique characters multiplied by the highest frequency we have seen, then everyone must have the exact same count. It is a quick and elegant way to verify balance instantly.
'''
def longestBalancedSubstring(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        freq = [0] * 26
        distinct = 0
        max_freq = 0

        for j in range(i, n):
            idx = ord(s[j]) - ord('a')

            # If character appears first time
            if freq[idx] == 0:
                distinct += 1

            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            length = j - i + 1

            # Balanced condition:
            # total length == distinct characters * frequency
            if length == distinct * max_freq:
                max_len = max(max_len, length)

    return max_len


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
print("Longest balanced substring length:", longestBalancedSubstring(s))
