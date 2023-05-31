from decimal import Decimal, Context, ROUND_DOWN

def mathparser(expression):
    # Remove whitespace from the expression
    expression = expression.replace(" ", "")

    # Define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # Helper function to apply operator to operands
    def apply_operator(operators, operands):
        operator = operators.pop()
        right_operand = operands.pop()
        left_operand = operands.pop()

        if operator == "+":
            result = left_operand + right_operand
        elif operator == "-":
            result = left_operand - right_operand
        elif operator == "*":
            result = left_operand * right_operand
        elif operator == "/":
            result = left_operand / right_operand

        operands.append(result)

    # Initialize stacks for operators and operands
    operators = []
    operands = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Find the complete number and append it to the operands stack
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == "."):
                j += 1
            number = Decimal(expression[i:j])
            operands.append(number)
            i = j
        elif expression[i] in "+-*/":
            # Apply operators with higher precedence before pushing the current operator
            while (
                operators and operators[-1] in "+-*/" and
                precedence[expression[i]] <= precedence[operators[-1]]
            ):
                apply_operator(operators, operands)

            # Push the current operator onto the stack
            operators.append(expression[i])
            i += 1
        elif expression[i] in "{[(":
            # Push opening parentheses onto the stack
            operators.append(expression[i])
            i += 1
        elif expression[i] in "}])":
            # Apply operators until an opening parentheses is encountered
            while operators and operators[-1] not in "{[(":
                apply_operator(operators, operands)

            # Pop the opening parentheses from the stack
            if operators and operators[-1] in "{[(":
                operators.pop()

            i += 1
        else:
            i += 1

    # Apply remaining operators in the stack
    while operators:
        apply_operator(operators, operands)

    # The final result will be the only element remaining in the operands stack
    result = operands[0]

    # Format the result to remove trailing zeros while preserving significant digits
    result_str = str(result)
    if result == int(result):
        result_str = str(int(result))

    print(f"mathparse result: {result_str}")

    return result_str

# Test the parser
#expression = "2000 + 5000"
#result = mathparser(expression)
#print(f"The result of '{expression}' is: {result}")