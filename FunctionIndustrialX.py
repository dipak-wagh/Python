# Procedural
def CheckEven(No):
   if(No % 2 == 0):
     return True
   else :
     return False


def main():
    value = 0
    Ret = False

    print("Enter number:")
    value = int(input())

    Ret = CheckEven(value)
    if(Ret == True):
       print("It is Even")
    else:
       print("It is Odd")


if __name__ == "__main__":
    main()