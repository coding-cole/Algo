for x in range(1, 21):
    if x%3 ==0 and x%5 == 0:
        print("FizzBuzz")
    elif x%5 ==0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    else:    
        print(x)

# EITHER OF THIS WILL WORK

for x in range(1, 21):
    if x%3 == 0:
        if x%5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif x%5 == 0:
        if x%3 == 0:
            print("FixxBuzz")
        else:
            print("Buzz")
    else:
        print(x)
    