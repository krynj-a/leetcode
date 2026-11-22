# 155. Min Stack
# https://leetcode.com/problems/min-stack/
#
# Idea: суть в том, что мы помимо обычного стака - храним стак найменьших чисел, чтобы не вычислять найменьшее число, перебирая массив, при вызове гетМин. стак обновляется в методах пуш - добавление числа, если оно меньше послденего минимального и поп - удаление.
# Вжано: идея работает только в случае, если можно удалять только последний элемент. 
# Time:  push O(1)  pop O(1)  top O(1)  getMin O(1)   Space: O(n)


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack)==1 or self.min[-1][0] > val:
            self.min.append([val, len(self.stack)-1])

    def pop(self) -> None:
        if self.min[-1][0] == self.stack[-1] and self.min[-1][1] == len(self.stack)-1:
            self.min.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min[-1][0]



s = MinStack()
s.push(3)
s.push(2)
s.push(1)
s.pop()
s.pop()
print(s.getMin())  # expected 3
