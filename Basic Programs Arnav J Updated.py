
num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))

print("\nChoose your operation: 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division")
choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(num_1 + num_2)
elif choice == 2:
    print(num_1 - num_2)
elif choice == 3:
    print(num_1 * num_2)
elif choice == 4:
    print(num_1 / num_2)
else:
    print("Invalid choice", "\nRun the program again and choose a valid option.")


n = float(input("Enter your number: "))

if n < 0:
    print("Your number is negative")
elif n > 0:
    print("Your number is positive")
else:
    print("Your number is zero")
