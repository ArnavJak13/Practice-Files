#Write a python program to print the following as an output statement:

#Student Name:
#Address:
#Contact Number:
#Mother Tongue:
#School Name:
#Year:
#Panel:
#Roll no:

student_name = str(input("Student Name:"))
address = str(input("Address:"))
contact_no = int(input("Contact Number:"))
mother_tongue = str(input("Mother Tongue:"))
school_name = str(input("School Name:"))
year = int(input("Year:"))
Panel = int(input("Panel:"))
roll_no = int(input("Roll no:"))

#Cube of a number
for i in range (5):
    num = int(input("Enter a number"))
    cube = num**3
    print("Cube:", cube)


#Reverse of a number
num = int(input("Enter a number:"))
reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num//10
print("Reverse:", reverse)



#Leap year
year = int(input("Enter a year:"))

if year % 400 == 0:
    print("The year is a leap year.")
elif year % 100 == 0:
    print("The year is not a leap year.")
else:
    print("The year is not a leap year.")

# a) Find similar elements and their index values
numbers = []
for i in range (2):
    num = int(input("Enter a number:"))
    numbers.append(num)
    print("\nList:", numbers)
    print("\nSimilar elements and their Index values:")
for i in range (2):
    if numbers.count(numbers[i]) > 1:
        print(numbers [i], "->", end = " ")
for j in range (2):
    if numbers [j] == numbers [i]:
        print(j, end = " ")
print()

# b) Count even and odd values
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2==0:
        even_count += 1
    else:
        odd_count += 1