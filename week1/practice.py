# Exercise 1

x = int(input("Enter a number: "))

if x < 0:
    print("Negative")
elif x > 0:
    print("Positive")
else:
    print("Zero")


# Exercise 2

x = int(input("Enter a temperature: "))

if x >= 30:
    print("Hot")
elif x >= 20:
    print("Warm")
else:
    print("Cold")


# Exercise 3

age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("Allowed")
else:
    print("Not allowed")


# Exercise 4

day = input("Enter a day: ")

if day == "Saturday" or day == "Friday":
    print("Weekend")
else:
    print("Weekday")


# Exercise 5

def main():
    ans = input("Are you a student? ")

    if is_student(ans):
        print("You are a student")
    else:
        print("You are not a student")


def is_student(x):
    if x == "yes":
        return True
    else:
        return False


main()


# Exercise 6

x = int(input("Enter a number: "))

match x:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")