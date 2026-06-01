def calc(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            return "Division by zero!"
        return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
print("1) Calculator result:", calc(num1, num2, op))


get_last_digit = lambda n: n % 10

user_num = int(input("\nEnter a number to get its last digit: "))
print("2) Last digit:", get_last_digit(user_num))


numbers_input = input("\nEnter numbers separated by space for squaring: ")
numbers = [int(x) for x in numbers_input.split()]
squares = list(map(lambda x: x * x, numbers))
print("3) Squared numbers:", squares)


words_input = input("\nEnter words separated by space: ")
words = words_input.split()
long_words = list(filter(lambda word: len(word) > 5, words))
print("4) Long words:", long_words)


students = [
    {"name": "Ivan", "age": 18},
    {"name": "Olya", "age": 20},
    {"name": "Max", "age": 17}
]
sorted_students = sorted(students, key=lambda student: student["age"])
print("\n5) Sorted students:", sorted_students)