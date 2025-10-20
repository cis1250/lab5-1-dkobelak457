#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#While loop takes the user input and checks if it is a valid integer
def get_input():
    while True:
        n = input("Enter how many Fibonacci Sequence integers do you want: ")
        if n.isdigit():
            n = int(n)
            if n > 0:
                return n
            print("Choose a positive integer ")
        else:
            print("Invalid, enter a whole number ")

def generate_fibonacci(n):
    a = 0
    b = 1
    #for loop takes a then calculates the next fib num using the t as a temp variable
    #saves the old value of a, updates a and b to move the sequence forwards
    for i in range(n):
        print(a, end=" ")
        t = a
        a = b
        b = t + b

def print_fibonacci():
    n = get_input()
    generate_fibonacci(n)

print_fibonacci()
