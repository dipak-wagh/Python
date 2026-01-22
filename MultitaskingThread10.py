import threading

def sumEven(No):
    sum = 0
    for i in range(2,No+1,2):
        sum = sum + i 

    print("Even sum is :",sum)

def sumOdd(No):
    sum = 0
    for i in range(1,No+1,2):
        sum = sum + i 

    print("Odd sum is :",sum)

def main():
    sumEven(100000000)
    sumOdd(100000000)

if __name__ == "__main__":
    main()