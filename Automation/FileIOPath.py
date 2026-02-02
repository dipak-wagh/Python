import os

def main():
    FileName = input("Enter the name of the file : ")

    Ret = os.path.isabs(FileName)

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It is relative path")
        

    if(Ret == True):
        fobj = open(FileName,"r")
        print("File gets successfully opened")

    else:
        print("There is no such file")


if __name__ == "__main__":
    main()