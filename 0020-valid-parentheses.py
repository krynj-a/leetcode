# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
#
# Idea: Суть в том, что мы создаем очередь скобок в эвейт бракетах и если этот стек не соблюдается - т.е. закрытая скобочка не сответствует послдней открытой, то мы выдаем фолс.
# Очень важны ещё проверки на то - существуют ли элементы в очереди(await_brackets), чтобы избежать аут оф рендж ситуации, когда изначально идет только закрытая скобка. Вторая же проверка
# создана для того, чтобы понять - обслужили ли мы все скобки.
# Time: O(n)   Space: O(1)


class Solution:
    def isValid(self, s: str) -> bool:
        await_bracket = []

        brackets_closed = {
            "}":"{",
            ")":"(",
            "]":"[",
        }
        for bracket in s:
            if bracket not in brackets_closed:
                await_bracket.append(bracket)
                continue

            if not await_bracket or brackets_closed[bracket] != await_bracket[-1]:
                return False
            else:
                await_bracket.pop()

        if not await_bracket:
            return True

        return False


print(Solution().isValid("()"))      # expected True
print(Solution().isValid("()[]{}"))  # expected True
print(Solution().isValid("(]"))      # expected False
print(Solution().isValid("([])"))    # expected True
print(Solution().isValid("([)]"))    # expected False
print(Solution().isValid("("))       # expected False
print(Solution().isValid(")"))       # expected False
