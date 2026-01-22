# Procedural
def CheckEven(No):
   if(No % 2 == 0):
    print("It is Even")
   else :
    print("It is Odd")

def main():
    value = 0

    print("Enter number:")
    value = int(input())

    CheckEven(value)



if __name__ == "__main__":
    main()