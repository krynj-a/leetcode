# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Idea: проходим перебирая сумму. вначале просто близстоящих пар. суть в том, что массив сортирован, и по условию - всегда содержит ровно одно решение -> когда сума больше
# я возвращаюсь обратно и иду назад - вопрос почему всегда находится число - мне честно самому не понятен
# Time: O(n) - в худшем случае массив пройдется два раза вперед, а потом назад. Space: O(1)


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        idx = 0
        jdx = 1
        while True:
            
            if numbers[idx] + numbers[jdx] == target:
                return [idx+1, jdx+1]
            elif numbers[idx] + numbers[jdx] > target:
                idx -= 1 
                continue
            jdx += 1
            idx += 1

    # Review 2026-11-19: classic converging pointers — left at the start, right at the end
# Idea: по-факту все то же самое, но суть в том, что мы просто берем и соединяем найменьшее число с найбольшим - таким образом, если найменьшее + найбольшее - больше таргета - нам нужно уменьшить сумму
# следовательно нужно двинуть правый поинтер влево. если же сума меньше - надо двинуть левый поинтер вправо, таким образом мы и приходим к ответу
# Time: O(n). Space: O(1)
    def twoSumClassic(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while left != right:
            
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1 
                continue
        
            left += 1            


print(Solution().twoSum([2, 7, 11, 15], 9))  # expected [1, 2]
print(Solution().twoSum([2, 3, 4], 6))       # expected [1, 3]
print(Solution().twoSum([-1, 0], -1))        # expected [1, 2]

print("--- classic ---")
print(Solution().twoSumClassic([2, 7, 11, 15], 9))  # expected [1, 2]
print(Solution().twoSumClassic([2, 3, 4], 6))       # expected [1, 3]
print(Solution().twoSumClassic([-1, 0], -1))        # expected [1, 2]
