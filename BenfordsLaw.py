from datetime import datetime
import math
import matplotlib.pyplot as plt
import numpy as np


# Will return an array with the numbers in the Fibonacci sequence of size of num
def fibonacci(arr, num):
    digitsDict = {}
    arr.append(1)
    arr.append(1)
    next = 0
    for i in range(2, num + 2):
        firstDigit = first_n_digits(arr[0], 1)
        if firstDigit in digitsDict:
            digitsDict[firstDigit] += 1
        else:
            digitsDict[firstDigit] = 1
        next = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = next  
    
    
    digitsArr = sorted(digitsDict.items(), key=lambda x: x[1], reverse=True)
    for i in digitsArr:
        print("% d : % d"%(i[0], i[1]))
    return digitsArr


def first_n_digits(num, n):
    return num // 10 ** (int(math.log10(num)) - n + 1)

def graphResults(digitsArr):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(range(1, 10), list(map(lambda x: x[1], digitsArr)), color='tab:blue')

    plt.show()


arrFib = []

num = int(input("Enter a number:"))
start = datetime.now()
arrFib = fibonacci(arrFib, num)
end = datetime.now()
graphResults(arrFib)
print("It took %.03f seconds"%((end-start).total_seconds()))
