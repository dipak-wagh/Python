import multiprocessing
import time
import os

def sumEven(No):
    print("PID of sumeven",os.getpid)
    print("PPID of sumeven",os.getppid)
    sum=0
    for i in range(2,No+1,2):
        sum=sum+i

    print("Even Sum is:",sum)

def sumOdd(No):
    print("PID of sumOdd",os.getpid)
    print("PPID of sumOdd",os.getppid)
    sum=0
    for i in range(1,No+1,2):
        sum=sum+i

    print("Odd sum is:",sum)

def main():
    print("PID of main",os.getpid)
    print("PPID of main",os.getppid)
    start_time = time.time()

    t1 = multiprocessing.Process(target=sumEven,args=(100000000))
    t2 = multiprocessing.process(target=sumOdd,args=(100000000))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Time required:",end_time - start_time)


if __name__ == "__main__":
    main()