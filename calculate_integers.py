# Calculate integers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

num = 1
a, b, c, d = (int(input(f"Enter {nu} number: ")) for num in range(4))

answer = (a**b) + (c**d)

print(answer)
