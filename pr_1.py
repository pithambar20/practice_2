def factorial(n1):
    if n1 < 0:
        return "Factorial is not defined for negative numbers"
    elif n1 == 0 or n1 == 1:
        return 1
    else:
        result = 1
        for i in range(2, n1 + 1):
            result *= i
        return result

print(factorial(5))  # Output: 120