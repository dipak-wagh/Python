def main():
    Ans = 0
    try:
        print("Inside try")

        print("Enter first number:")
        No1 = int(input())

        print("Enter second number:")
        No2 = int(input())
        
        Ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Inside except : ",zobj)

    except ValueError as vobj:
        print("Insode except : ",vobj)

    except Exception as eobj:
        print("Inside except : ",eobj)
    finally:
        print("Inside finally")

    print("Divison is : ",Ans)    


if __name__ == "__main__":
    main()