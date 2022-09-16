class OperationFunctions:
    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        return num1*num2

    @staticmethod
    def division(num1, num2):
        return num1/num2

class Expression:
    priorities = {'+' : 1, '-': 2, '*': 3, '/': 4}
    opertations = {'+': OperationFunctions.addition, '-': OperationFunctions.subtraction, '*': OperationFunctions.multiplication, '/': OperationFunctions.division}

    def __init__(self):
        self.opr = []
        self.numbers = []
        

class NoBracketExpression(Expression):
    def __init__(self, vals):
        self.opr = []
        self.numbers = []
        for i in vals:
            if i in self.priorities:
                self.opr += [i]
            else:
                self.numbers += [i]

    def evaluate(self):
        stack = []
        count = 0
        while count != len(self.opr) - 1:
            if self.priorities[self.opr[count]] <= self.priorities[self.opr[count + 1]]:
                stack.append(count)
            else:
                stack.append(count)
                count -= len(stack)
                self.removeStack(stack)

            count += 1
            
        stack.append(len(self.opr) - 1)
        self.removeStack(stack)
        self.answer = self.numbers[0]

        return self.answer

                    

    def removeStack(self, stack):
        while stack != []:
            i = stack.pop()
            num1 = self.numbers.pop(i)
            num2 = self.numbers.pop(i)
            self.numbers.insert(i, self.opertations[self.opr[i]](num1, num2))
            self.opr.pop(i)
            
class BracketExpression(Expression):
    def __init__(self, expr):
        stack = []
        currStr = ''
        isExpr = False
        for i in expr:
            if i in self.priorities:
                if isExpr:
                    currStr += i
                else:
                    stack.append(float(currStr))
                    currStr = i
                    isExpr = True
            elif i == '(':
                if currStr != '':
                    stack.append(currStr)
                isExpr = False
                stack.append('(')
                currStr = ''
            elif i == ')':
                stack.append(float(currStr))
                isExpr = True
                currStr = ''
                c = stack.pop()
                expr = []
                while c != '(':
                    expr.append(c)
                    c = stack.pop()

                val = NoBracketExpression(expr[::-1]).evaluate()
                stack.append(val)
            elif i.isnumeric():
                if isExpr:
                    stack.append(currStr)
                    currStr = i
                    isExpr = False
                else:
                    currStr += i

        if currStr != '':
            stack.append(float(currStr))

        self.answer = NoBracketExpression(stack).evaluate()