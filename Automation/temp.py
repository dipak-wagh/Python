from MarvellousFMR import filterX, mapX, reduceX

checkEven = lambda No: (No % 2 == 0)
Increment = lambda No: (No + 1)
Add = lambda A,B : A + B

def main():
    Data = [11,10,12,20,24]
    print("Actual Data is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data After filter is : ",FData)

    MData = list(mapX(Increment,FData))
    print("Data After Map is : ",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
