#!/usr/bin/env python3

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

def gen_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = b
        b = t + b
        yield t

def print_fib(sequence):
    for num in sequence:
        print(num, end=" ")
    print()

def fibonacci():
    n = get_input()
    print_fib(gen_fibonacci(n))
fibonacci()
