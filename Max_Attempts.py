def Max_Attempts():
    print("_" * 100)
    print("Write 'N' If You Don't Want to Give Below Details , Will Have 3 Que")
    print("If You Type N Then Will Try From Start to end")
    print("_" * 100)
    User_Password_Length = input("What Is Length Of Your Password (Optional) -----> ")
    User_Password_Max_Length = input("What Is Max Char In Your Password (Optional) -----> ")
    User_Password_Min_Length = input("What Is Min Char In Your Password (Optional) -----> ")

    if User_Password_Length == 'N' or User_Password_Max_Length == 'N' or User_Password_Min_Length == 'N':
        print("User You Don't Have Any Special Details About Password")
        print("So , You Don't Have Any Quantity Of Max Attempts :)")
        print("Now Program Will Start From Scrach")