# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
#
# Idea: сортируем слово и добавляем в качестве ключа в словарь, таким образом сортируем аннограммы
# Time: O(nlogn) - потому что проход по массиву n, но сортировка каждого слова из TimSort klogk, где К - это длинна слова   Space: O(n) - словарь записывает весь массив


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram =  {}
        for word in strs:
            sort_ann = str(sorted(word))
            if  sort_ann not in anagram:
                anagram[sort_ann] = []
            anagram[sort_ann].append(word)
        
        return list(anagram.values())
           
             


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# expected (any order): [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
print(Solution().groupAnagrams([""]))   # expected [[""]]
print(Solution().groupAnagrams(["a"]))  # expected [["a"]]


# Неудачный вариант
# def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#        annograms =  {}
#        for i in range(len(strs)):
#             total = 0
#             for c in strs[i]:
#                 total += ord(c)
#             if total not in annograms:
#                 annograms[total] = [strs[i]]
#                 continue
#             annograms[total].append(strs[i])
#        answer = []
#        for key in annograms:
#            answer.append(annograms[key])   
#        return answer