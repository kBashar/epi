number = int(input("Enter a number: ")) # Get the number from the user

result = 0 # Initialize the result to 0

while number:
    result = result ^ 1
    number &= (number -1)

print(f'parity is {result}')


'''
Rationale:

Here we are counting number of 1s using another properties of binary numbers.

In binary numbers among two consecutive numbers, 
let's say two numbers are X and X-1, 
The Position of the first set bit from right to left in X is same as
The Position of the first unset bit from right to left in X-1.

All bits on the left of that bit are flipped in two numbers and
All bits on the right of that bit are same in two numbers.

This propertry can be used to unset the least set bit in number. 

This gives us a way to run the counting loop only K times where 
    K is the count of set bits(1s) in a number.

Example: 
        Flipping point 
         ↓  
X   4 -- 100
X-1 3 -- 011  

Here
    100 
&   011
------- 
    000 
'''