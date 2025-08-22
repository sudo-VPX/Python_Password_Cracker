#Library

import time
import string

#Self Made Library

import ASCII_Drawing

# Default Variables

K = 1000 #Thousand
M = 1000000 #Million
B = 1000000000 #Billion
T = 1000000000000 #Trillion
Q = 1000000000000000 #Quadrillion


# Functions

def Max_Attempts():
    print("Length Of Password Is ----> " + str(Length_Password))
    print("Total Words Allowed ----> " + str(All_Char_Len))
    Total_Max_Attempts = All_Char_Len ** Length_Password
    if Total_Max_Attempts >= Q:
        Total_Max_Attempts = str(round(Total_Max_Attempts / Q, 2)) + " Q"
    elif Total_Max_Attempts >= T:
        Total_Max_Attempts = str(round(Total_Max_Attempts / T, 2)) + " T"
    elif Total_Max_Attempts >= B:
        Total_Max_Attempts = str(round(Total_Max_Attempts / B, 2)) + " B"
    elif Total_Max_Attempts >= M:
        Total_Max_Attempts = str(round(Total_Max_Attempts / M, 2)) + " M"
    elif Total_Max_Attempts >= K:
        Total_Max_Attempts = str(round(Total_Max_Attempts / K, 2)) + " K"
    print("Total Max Attempts We Can Make (Approx) ----> " + str(Total_Max_Attempts))

# All Chracters Allowed Yet

All_Char = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation)
All_Char_Len = len(All_Char)
All_Char_Print = " , ".join(str(Char) for Char in All_Char)

# Main Logo Entrance 

time.sleep(0.1)
ASCII_Drawing.FeroFy_Logo()
time.sleep(0.1)
print ( "_" * 100 )
print("")
time.sleep(0.1)

# Some Details

print ( "User There This Is a Free Tool For Now , Just You Need To Know A Little Bit Of Python Which Is Optionl Enjoy :)" )
print("")
print ( "All Characters Allowed ---> " + All_Char_Print )
print("")

# Password Related

print("")
print ( "_" * 100 )
print("")
Password = str(input("Enter Your Password ---> "))
print("Write N If You Don't Want to Give Below Details")
User_Specific_Password_Length = input("What Is Length Of Your Password (Optional) -----> ")
Length_Password = len(Password)
print("")
print ( "_" * 100 )
print("")
Max_Attempts()

# Main Cracker

for i in range(0,1):
    print(All_Char[i])
    i=i+1

# Exit Pannel

print("")
print ( "_" * 100 )
print("")
print("You Can Exit Now")
Exit_Review = input("Your Experience Plz ------> ")