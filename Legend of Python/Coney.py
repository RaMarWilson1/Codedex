print("Enter your height in cm")
height = int(input())
print("Enter your credits")
credit = int(input())
if height >= 137 and credit >= 10:
    print("Enjoy the ride!")
elif height >= 137 and credit < 10:
    print("You don't have enough credits.")
elif height < 137 and credit >= 10:
    print("You are not tall enough to ride.")
else:
    print("you do not meet requirements")
