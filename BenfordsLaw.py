from datetime import datetime

def fibonacci(num):    
    count = 0
    n1, n2 = 1, 1
    nth = 0
    if num < 0:
        return 1
    while count < num:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1    
    return n1

def countFirstDigit(arr):
    Dict = {}
    for item in arr:         
        string = item[0]
        if string in Dict:
            Dict[string] += 1
        else:
            Dict[string] = 1
    Dict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    for i in Dict:
        print("% s : % d"%(i[0], i[1]))


arrFib = []

num = int(input("Enter a number:"))
start = datetime.now()
for i in range(0, num):
    arrFib.append(str(fibonacci(i)))
end2 = datetime.now()
print("On fibonacci funct %.03f"%(end2 - start).total_seconds())
#print(arrFib)
countFirstDigit(arrFib)
end = datetime.now()

print("It took %.3f seconds"%((end - start).total_seconds()))
