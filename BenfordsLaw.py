from datetime import datetime
import math

def fibonacci(arr, num):
    start2 = datetime.now()
    arr.append(1)
    arr.append(1)
    for i in range(2, num):
        arr.append(arr[i-2] + arr[i -1])    
    end2 = datetime.now()
    print("On fibonacci funct %.03f"%(end2 - start2).total_seconds())
    return arr

    

def countFirstDigit(arr):
    Dict = {}
    start1 = datetime.now()
    for item in arr:    
        firstDigit = first_n_digits(item, 1)
        if firstDigit in Dict:
            Dict[firstDigit] += 1
        else:
            Dict[firstDigit] = 1
    end1 = datetime.now()
    print("On first Digit funct %.03f"%(end1 - start1).total_seconds())
    Dict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    for i in Dict:
        print("% d : % d"%(i[0], i[1]))

def first_n_digits(num, n):
    return num // 10 ** (int(math.log10(num)) - n + 1)
    


arrFib = []

num = int(input("Enter a number:"))
start = datetime.now()

arrFib = fibonacci(arrFib, num)
#print(arrFib[num-1])

#print(arrFib)
countFirstDigit(arrFib)
end = datetime.now()

print("It took %.3f seconds"%((end - start).total_seconds()))
