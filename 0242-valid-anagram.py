# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
#
# Idea: Все просто - сортируем и проверяем совпадают ли все буквы - таким образом можно понять анаграма єто или нет. вначале делаем простую проверку по длинне, чтобы не сверять и не сортировать заведомо ненужные массивы
# Time: O(nlogn) - потому что используем Tim сорт два раза.   Space: O(n) - так как сорт создает новые списки


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        return sorted(s) == sorted(t)

print(Solution().isAnagram("anagram", "nagaram"))  # expected True
print(Solution().isAnagram("rat", "car"))          # expected False
print(Solution().isAnagram("ab", "a"))             # expected False
