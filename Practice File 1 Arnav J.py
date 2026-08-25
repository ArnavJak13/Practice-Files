
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

print("\nFirst number:", numbers[0])
print("Second number:", numbers[1])
print("Third number:", numbers[2])
print("Fourth number:", numbers[3])
print("Fifth number:", numbers[4])

numbers.append(60)
print("\nAfter Adding:", numbers)

element = int(input("Search for your number:"))
count = numbers.count(element)
if count > 0:
    print("Yes, your number is there",)
else:
    print("No, your number is not there")



numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

numbers.insert(1,15)
print("After Inserting:", numbers)

index = int(input("\nEnter the index to remove:"))
numbers.pop(index)
print("List after removal:", numbers)

element = int(input("Enter the element to remove:"))
numbers.remove(element)
print("List after removal:", numbers)