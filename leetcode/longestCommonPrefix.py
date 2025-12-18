class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = strs[0]
        max_len = 0

        for i in strs:
            len1 = len(i)
            if len1 < len(min_str):
                min_str = i
        for i in range(len(min_str)):
            for j in strs:
                if j[i] != min_str[i]:
                    max_len = i
                    return min_str[:max_len]
        return min_str