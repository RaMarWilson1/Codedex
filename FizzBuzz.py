for x in range(0, 100):
    if x % 3 == 0 and x % 2 == 0:
        print(str(x) + " Fizz \n Buzz")
    elif x % 3 == 0 and x % 2 != 0:
        print(str(x) + " Fizz\n")
    elif x % 3 != 0 and x % 2 == 0:
        print(str(x) + " Buzz\n")
    else:
        print(str(x) + " Not a FizzBuzz\n")
 v b        