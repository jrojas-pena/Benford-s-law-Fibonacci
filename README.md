# Introduction

This Python program checks if the Fibonacci sequence follows Benford's law. Benford's law is an empirical observation about the frequency distribution of leading digits in many naturally occurring sets of numerical data. The law states that in many naturally occurring sets of numerical data, the frequency of the leading digit is distributed in a specific way. Specifically, the probability that the first digit is d is given by:

P(d) = log10(1 + 1/d)

for d = 1, 2, ..., 9.

The program consists of two functions: fibonacci() and countFirstDigit().
# Requirements

This program requires the following:

   - Python 3.x
   - datetime module
   - math module

# How to use

   - Open a Python environment or a text editor that can run Python code.
   - Copy and paste the code into the environment or editor.
   - Run the program.
   - When prompted, enter a number.
   - The program will output the count of each digit in the first digit of each number in the Fibonacci sequence up to the entered number, as well as the time it took to run both functions.

# Functions
## fibonacci(arr, num)

This function takes two parameters:

    arr: an empty list
    num: the number up to which the Fibonacci sequence should be calculated

The function calculates the Fibonacci sequence up to the given number and returns the list of numbers.
## countFirstDigit(arr)

This function takes one parameter:

    arr: a list of numbers

The function checks whether or not the first digit of each number in the given list follows Benford's law. If the first digit distribution of the given list matches the distribution predicted by Benford's law, the function prints the frequency distribution of the first digit. If not, the function prints the frequency distribution of the first digit. The time it takes to run the function is printed.
## first_n_digits(num, n)

This function takes two parameters:

    num: a number
    n: an integer

The function returns the first $n$ digits of the given number. The first $n$ digits of a number can be found by dividing the number by $10^{\left\lfloor\log_{10} num\right\rfloor - n + 1}$. This can be expressed mathematically as:

$\text{first n digits} = \lfloor\frac{num}{10^{\left\lfloor\log_{10} num\right\rfloor - n + 1}}\rfloor$

For example, if num is 12345 and n is 3, the function would return the first three digits of the number, which is 123.

The function returns the first n digits of the given number.
