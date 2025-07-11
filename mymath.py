
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(n):
    return n * n


# Factorial using for loop
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


number = int(input("Enter a number: "))
print(f"Factorial of {number} is:", factorial(number))


# Factorial using recursion
def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is:", factorial_recursive(number))

# Palindrome - A word, number, phrase, or sequence that reads the same forward and backward.
#Palindrome Check for String
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("Hello"))
print(is_palindrome("nurses run"))

# Palindrome Check for Integer
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]


print(is_palindrome_number(121))
print(is_palindrome_number(123))

# Fibonacci - Each number is the sum of the two preceding ones.
# Fibonacci using for loop
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_series(15)


# armstrong Number - 153 = 1^3 + 5^3 + 3^3 = 1+125+27 = 153
# equal to the sum of its digits raised to the power of the number of digits.
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

for num in range(100, 1000):
    if is_armstrong(num):
        print(num, end=' ')

# sum of digits
# using while loop
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10       # Get the last digit
        total += digit         # Add it to total
        num = num // 10        # Remove the last digit
    return total

number = int(input("Enter a number: "))
print(f"Sum of digits:", sum_of_digits(number))

# Using str() and sum()
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

number = int(input("Enter a number: "))
print(f"Sum of digits:", sum_of_digits(number))

# Sorting
colors = ['Blue', 'Red', 'Green', 'Yellow', 'Orange']

# Ascending order (A to Z)
ascending = sorted(colors)
print("Colors in Ascending Order:", ascending)
#
# Descending order (Z to A)
descending = sorted(colors, reverse=True)
print("Colors in Descending Order:", descending)

# Using sort()
colors = ['Blue', 'Red', 'Green', 'Yellow', 'Orange']

# Ascending order (A to Z)
colors.sort()
print("Colors in Ascending Order:", colors)

# Descending order (Z to A)
colors.sort(reverse = True)
print("Colors in Descending Order:", colors)
