x = int(input("Please enter a number:\n"))

if x % 3 == 0:
     if x % 5 == 0:
          print("Your number is divisible by 3 and 5 ")
     else:
          print("Your number is divisible by 3 and NOT 5.")
elif x % 5 ==0:
    print("Your number is divisible by 5 and NOT 3.")
else:
    print("Your number is NOT divisible by 3 and 5.")
