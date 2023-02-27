from datetime import datetime
import math
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import colors
#from matplotlib.ticker import PercentFormatter


# Will return an array with the numbers in the Fibonacci sequence of size of num
def fibonacci(arr, num):
    arr.append(1)
    arr.append(1)
    for i in range(2, num):
        arr.append(arr[i-2] + arr[i -1])    
    return arr

    
# Counts the amount of times a specific digit appears as the first digit on the numbers inside the array (arr)
def countFirstDigit(arr):
    # Dictionary of digits
    digitsDict = {}

    for item in arr:    
        firstDigit = first_n_digits(item, 1)
        if firstDigit in digitsDict:
            digitsDict[firstDigit] += 1
        else:
            digitsDict[firstDigit] = 1

    digitsDict = sorted(digitsDict.items(), key=lambda x: x[1], reverse=True)
    for i in digitsDict:
        print("% d : % d"%(i[0], i[1]))
    return digitsDict

# Returns the first n digits in num
def first_n_digits(num, n):
    return num // 10 ** (int(math.log10(num)) - n + 1)

def graphResults(digitsDict):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(range(1, 10), list(map(lambda x: x[1], digitsDict)), color='tab:blue')

    plt.show()


arrFib = []

num = int(input("Enter a number:"))
arrFib = fibonacci(arrFib, num)
#print(arrFib[num-1])

#print(arrFib)
graphResults(countFirstDigit(arrFib))
