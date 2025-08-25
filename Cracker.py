#Library

import time
import string

#Self Made Library

import ASCII_Drawing
import Max_Attempts

# Default Variables

K = 1000 #Thousand
M = 1000000 #Million
B = 1000000000 #Billion
T = 1000000000000 #Trillion
Q = 1000000000000000 #Quadrillion

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
print("_" * 100)
print("")
print ( "All Characters Allowed ---> " + All_Char_Print )
print("")

# Password Related Things

Max_Attempts.Max_Attempts()

# Main Cracker

# Later Work :)

# Exit Pannel

print("")
print ( "_" * 100 )
print("")
print("You Can Exit Now")
Exit_Review = input("Your Experience Plz ------> ")