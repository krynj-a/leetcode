# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
#
# Idea: создаем алфавит принимаемых значений - фильтруем, проверяем две половины
# Time: O(3n/2)=O(n)   Space: O(n), m = alphabet.size

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        string = ""
        
        s = s.casefold()
        for ch in s:
            if alphabet.find(ch) != -1:
                string = string+ch
        string_size = len(string)
        for i in range(string_size//2):
            if string[i] != string[string_size-i-1]:
                return False
        return True

    # Review 2026-11-17: O(1) extra space — two pointers directly on s, no new string
    def isPalindromeO1(self, s: str) -> bool:
        string_size = len(s)
        right = string_size - 1
        left = 0
        while left < right:
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].isalnum():
                left += 1
                continue

            if s[left].lower() != s[right].lower():
                return False
           
            left += 1
            right -=1
        return True


print(Solution().isPalindrome("Live on evasions? No, I save no evil."))  # expected True
print(Solution().isPalindrome("race a car"))                      # expected False
print(Solution().isPalindrome("a ba"))                               # expected True

print("--- O(1) version ---")
print(Solution().isPalindromeO1("A man, a plan, a canal: Panama"))  # expected True
print(Solution().isPalindromeO1("race a car"))                      # expected False
print(Solution().isPalindromeO1(" "))                               # expected True
print(Solution().isPalindromeO1(".,"))                              # expected True
print(Solution().isPalindromeO1("0P"))                              # expected False
