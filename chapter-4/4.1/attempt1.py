number = int(input("Enter a number: ")) # Get the number from the user

result = 0 # Initialize the result to 0

while number:
    # we are bitmasking to find out if the LSB is set or not
    one_or_zero = number & 1
    # we only care if the number is odd or even, so storing `mod 2` of the result is enough
    result = result ^ one_or_zero
    # right shift `number` to bring the next bit to the end
    number >>=1

print(f'parity is {result}')


'''

'''
