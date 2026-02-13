'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
def evalRPN(tokens):
    stack = []

    for token in tokens:
        # If token is an operator, pop two numbers and calculate
        if token in {"+", "-", "*", "/"}:
            a = stack.pop()   # second operand
            b = stack.pop()   # first operand

            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(b * a)
            else:
                # Division should truncate toward zero
                stack.append(int(b / a))
        else:
            # Token is a number → push to stack
            stack.append(int(token))

    # Final result will be the only element left in stack
    return stack[0]


# ====== INPUT / OUTPUT ======
tokens = input("Enter RPN tokens separated by space: ").split()
print("Result:", evalRPN(tokens))
