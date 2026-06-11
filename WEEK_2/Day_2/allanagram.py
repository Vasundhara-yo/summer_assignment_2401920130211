class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        result = []

        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                result.append(i - len(p) + 1)

        return result