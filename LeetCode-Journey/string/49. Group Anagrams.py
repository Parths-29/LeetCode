def groupAnagrams(strs):
    '''
    Approach:

    1️⃣ For each word, sort its characters.
    2️⃣ Use the sorted word as a key in a dictionary.
    3️⃣ Append the original word to that key.
    4️⃣ Return all grouped values.
    '''

    anagram_map = {}

    for word in strs:
        # Sort characters to form key
        key = ''.join(sorted(word))

        if key not in anagram_map:
            anagram_map[key] = []

        anagram_map[key].append(word)

    return list(anagram_map.values())


# ====== INPUT / OUTPUT ======
strs = input("Enter words separated by space: ").split()
print("Grouped anagrams:", groupAnagrams(strs))
