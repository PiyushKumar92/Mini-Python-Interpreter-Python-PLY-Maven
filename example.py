# Simple program to demonstrate the compiler features

# Variable assignment and arithmetic
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y

# Print statements
print("Hello, World!")
print("Basic arithmetic operations:")
print("x =", x)
print("y =", y)
print("x + y =", sum)
print("x - y =", difference)
print("x * y =", product)
print("x / y =", quotient)

# Conditional statement
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Loop with a range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Simple function definition and call
def add(a, b):
    return a + b

result = add(x, y)
print("Function result:", result)

# List operations
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("First element:", numbers[0])
print("List length:", len(numbers))

# String operations
message = "hello"
print("Original message:", message)
print("Uppercase:", message.upper())