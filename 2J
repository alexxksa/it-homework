# 1
while True:
    try:
        user_number = float(input("Task 1: Enter a number: "))
        print("Success! Your number is:", user_number)
        break
    except ValueError:
        print("That is not a number. Please try again.")


# 2
print("\nTask 2: Calculator Menu")
print("1 — +")
print("2 — -")
print("3 — *")
print("4 — /")

try:
    choice = input("Choose operation (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Error: Invalid menu choice!")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", num1 / num2)
except ValueError:
    print("Error: Please enter valid numbers!")


# 3
name = input("\nTask 3: Enter your name: ")
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            print(f"Hello {name}, your age is {age}")
            break
        else:
            print("Age must be between 1 and 120. Try again.")
    except ValueError:
        print("Age must be a whole number. Try again.")


# 4
my_list = [10, 20, 30, 40, 50]
print("\nTask 4: List is", my_list)
try:
    index = int(input("Enter an index (0-4) to get a value: "))
    print("Value at index:", my_list[index])
except ValueError:
    print("Error: Index must be a whole number!")
except IndexError:
    print("Error: Index out of range! Choose between 0 and 4.")


# 5
print("\nTask 5: Trying to read file...")
filename = "test_file.txt"
try:
    with open(filename, "r") as file:
        print("File content:", file.read())
except FileNotFoundError:
    print(f"The file '{filename}' does not exist, but the program did not crash!")


# 6
print("\nTask 6: Currency Converter (USD to EUR)")
try:
    rate = 0.92
    usd_input = input("Enter USD amount to convert: ")
    usd = float(usd_input)
    if usd < 0:
        print("Error: Amount cannot be negative!")
    else:
        eur = usd * rate
        print(f"{usd} USD is {eur:.2f} EUR")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")


# 7
print("\nTask 7: Custom Game Character program")
try:
    hp_input = input("Enter character health points (HP): ")
    hp = int(hp_input)
    
    level_input = input("Enter character level: ")
    level = int(level_input)
    
    damage_input = input("Enter incoming damage: ")
    damage = int(damage_input)
    
    current_hp = hp - damage
    print(f"Character Level {level} now has {current_hp} HP left!")
except ValueError:
    print("Custom Error 1: All stats must be whole numbers!")
except Exception as e:
    print("Custom Error 2: Something unexpected went wrong!")
