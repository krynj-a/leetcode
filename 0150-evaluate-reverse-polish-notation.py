# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Idea: creating a stack for numbers and operator dictionary to determine needed functions and use them on stack objects according to their appearance in tokens list 
# Time: O(n)   Space: O(n)


class Solution:
    actions = {
        "+": lambda x,y: x + y,
        "*": lambda x,y: x * y,
        "-": lambda x,y: x - y,
        "/": lambda x,y: int(x / y),
    }
    
    def evalRPN(self, tokens: list[str]) -> int:
        rpn_stack = []
        
        for token in tokens:
            if token not in self.actions: 
                rpn_stack.append(int(token))
                continue
            right = rpn_stack.pop()
            left = rpn_stack.pop()
            rpn_stack.append(self.actions[token](left,right))

        return rpn_stack[0]


s = Solution()
print(s.evalRPN(["3", "4", "-"]))             # expected -1
print(s.evalRPN(["42"]))                      # expected 42
print(s.evalRPN(["1", "2", "+", "3", "4", "+", "*"]))  # expected 21
print(s.evalRPN(["2", "3", "4", "*", "-"]))   # expected -10
print(s.evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # expected 14
print(s.evalRPN(["-7", "2", "/"]))            # expected -3
