import threading
import time

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
    star_time = time.time()
    sumEven(100000000)
    sumOdd(100000000)
    end_time = time.time()

    print("Time Required :", end_time-star_time)

if __name__ == "__main__":
    main()