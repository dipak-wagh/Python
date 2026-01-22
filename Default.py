
def EmployeeInfo(Name = "Ajay",Age = 21, Salary = 1000, City = "Mumbai"):
    print("Name:",Name)
    print("Age:",Age)
    print("Salary",Salary)
    print("City:",City)
    print("")

def main():    
    EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50)   #Correct

if __name__ == "__main__":
    main()