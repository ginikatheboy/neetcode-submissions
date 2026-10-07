class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_num = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)

            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(cur_num)
                elif sign == "-":
                    stack.append(-cur_num)
                elif sign == "*":
                    stack.append(stack.pop() * cur_num)
                else:
                    stack.append(int(stack.pop() / cur_num))

                sign = char
                cur_num = 0

        return sum(stack)

        