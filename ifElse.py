age = int(input("Enter your age (1-80) :"))
print(f"Your age is {age}")

if(age > 18):
    print("you can drive")
elif(age >= 18):
    print("you can drive.")
else:
    print("you can't drive")


# Nested ifElse

num = 18

if (num < 18):
    print("you are not allowed to do certain work.")
elif(num > 18):
    if(num <= 10):
        print("Number is between 1-10 you are too ")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero.")