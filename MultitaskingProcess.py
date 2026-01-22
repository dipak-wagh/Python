import multiprocessing
import time
import os

def sumEven(No):
    print("PID of sumEven :", os.getpid())    #51
    print("PPID of sumEven :", os.getppid())  #21
    sum = 0
    for i in range(2,No+1,2):
        sum = sum + i 

    print("Even sum is :",sum)

def sumOdd(No):
    print("PID of sumOdd :", os.getpid())  #101
    print("PPID of sumOdd :", os.getppid())  #21
    
    sum = 0
    for i in range(1,No+1,2):
        sum = sum + i 

    print("Odd sum is :",sum)

def main():
    print("PID of main :", os.getpid())      #21  
    print("PPID of main :", os.getppid())   #11

    star_time = time.time()
    
    t1 = multiprocessing.Process(target=sumEven, args=(100000000,))
    t2 = multiprocessing.Process(target=sumOdd, args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.time()

    print("Time Required :", end_time-star_time)

if __name__ == "__main__":
    main()