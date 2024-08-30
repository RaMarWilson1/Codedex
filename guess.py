tries=0
guess = 0
while tries != 6:
   if guess == int(input("Guess the number:  ")):
       print("You got it!")
       break
   else:
       print("Sorry try again")
       tries = tries+1
