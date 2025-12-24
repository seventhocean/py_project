## leetcode/reverseWords.py

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split()
#         return ' '.join(reversed(words))

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i  -= 1
                continue
            j = i
            while i>= 0 and s[i] != ' ':
                i -= 1
                res.append(s[i+1:j+1])
        return ' '.join(res)


# Example usage:
sol = Solution()
sentence = input("Enter a sentence: ")
print(sol.reverseWords(sentence))  # Output: "blue is sky the"