number = int(input("Enter a number:"))

# We bitmask to check if the LSB is `one` or `zero`.
result = number & 1

# A binary number that has 1 in LSB is Odd and even if it has 0.
print(f'This number is {"Odd" if result == 1 else "Even"}')