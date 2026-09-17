
# 1. Write a python program that accepts the three numbers from user and display its addition using functions.

x = int(input("Enter value of x:"))
y = int(input("Enter value of y:"))
z = int(input("Enter value of z:"))

def cal_sum(x, y, z):
    sum = x + y + z
    return sum

s = cal_sum(x, y, z)
print(s)


# 2. Write a Python program to receive three integers from keyboard
# and get their sum and product calculated through a user-defined function cal_sum_prod().

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

def cal_sum_prod(x, y, z):
    sum = x + y + z
    product = x * y * z
    return sum, product

s, p = cal_sum_prod(x, y, z)

print(s, p)


# 3. Write a python program to accept the number from the user and display prime factors of that number.

num = int(input("Enter your number: "))

print("Prime factors are:")

def prime_factors(num):
    factor = 2

    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num // factor
        else:
            factor = factor + 1

prime_factors(num)



# 4. Write a python program whcih will print all even numbers in a range 1 to 100.

for i in range(1, 101):
    if i % 2 == 0:
        print(i)