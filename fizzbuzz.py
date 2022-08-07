print("Hello")
while True:
    try:
        numRange = int(input("Enter a number range to check: "))
        if numRange < 0:
            print("Sorry, the number range must be a positive value, try again")
            continue
        break
    except:
        print("You didn't enter a valid number, please try again.")
numArray = []
for i in range(numRange + 1):
    if i % 3 == 0 and i % 5 == 0:
        numArray.append("FizzBuzz")
        continue
    elif i % 3 == 0:
        numArray.append("Fizz")
        continue
    elif i % 5 == 0:
        numArray.append("Buzz")
        continue
    numArray.append(i)
for i in numArray:
    print(i, end=" ")