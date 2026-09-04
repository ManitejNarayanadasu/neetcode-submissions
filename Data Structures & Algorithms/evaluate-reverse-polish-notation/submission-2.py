class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = []
        for i in tokens:
            if i not in ('+','-','*','/'):
                calc.append(int(i))
            else:
                b = calc.pop()
                a = calc.pop()
                if i == '+':
                    calc.append(a+b)
                elif i == '-':
                    calc.append(a-b)
                elif i == '*':
                    calc.append(a*b)
                else:
                    calc.append(int(a/b))
        return calc[0]    

        