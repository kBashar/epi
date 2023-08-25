'''
Problem: 
    Check if a number is Odd or Even without using Modular arithmatic.

Solution: 
    Binary representation of a number holds 0 in its LSB(Least Significant Bit) if it
    is an Even number. On the other hand LSB will be 1 if the number is Odd.

    So, We can bitmask a number at LSB to check if the bit is set or not to tell if the
    number is odd or even.

Example:
    Decimal     Binary      LSB     Type
    ------------------------------------
    5           101         1       Odd
    6           110         0       Even
    34          100010      0       Even
    67          1000011     1       Odd

'''

number = int(input("Enter a number:"))

# We bitmask to check if the LSB is `one` or `zero`.
result = number & 1

# A binary number that has 1 in LSB is Odd and even if it has 0.
print(f'This number is {"Odd" if result == 1 else "Even"}')