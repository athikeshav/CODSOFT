# Calculator

def calculation(num1, num2, op):
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation. "
    return result

print("Calculator:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operation to be performed (+, -, *, /): ")

final_result = calculation(num1, num2, op)
print("Result:", final_result)
