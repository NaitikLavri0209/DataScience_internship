import random

students = {}


def calculator():
    print("\nCalculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+,-,*,/): ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b == 0:
                print("Division by zero not allowed")
            else:
                print("Result:", a / b)
        else:
            print("Invalid operator")

    except:
        print("Invalid Input")


def factorial():
    try:
        n = int(input("Enter number: "))
        fact = 1

        for i in range(1, n + 1):
            fact *= i

        print("Factorial =", fact)

    except:
        print("Invalid Input")


def fibonacci():
    n = int(input("How many terms: "))

    a = 0
    b = 1

    print(a, end=" ")

    for i in range(n - 1):
        print(b, end=" ")
        c = a + b
        a = b
        b = c

    print()


def prime():
    n = int(input("Enter number: "))

    if n < 2:
        print("Not Prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")


def palindrome():
    text = input("Enter text: ")

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


def armstrong():
    n = int(input("Enter number: "))

    temp = n
    s = 0

    while temp > 0:
        d = temp % 10
        s += d ** len(str(n))
        temp //= 10

    if s == n:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


def even_odd():
    nums = []

    n = int(input("How many numbers: "))

    for i in range(n):
        nums.append(int(input()))

    even = 0
    odd = 0

    for i in nums:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd :", odd)


def largest_smallest():
    nums = []

    n = int(input("How many numbers: "))

    for i in range(n):
        nums.append(int(input()))

    print("Largest :", max(nums))
    print("Smallest:", min(nums))


def bubble_sort():
    nums = []

    n = int(input("How many numbers: "))

    for i in range(n):
        nums.append(int(input()))

    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)


def linear_search():
    nums = []

    n = int(input("How many numbers: "))

    for i in range(n):
        nums.append(int(input()))

    key = int(input("Enter number to search: "))

    if key in nums:
        print("Found at index", nums.index(key))
    else:
        print("Not Found")


def temperature():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    ch = int(input("Choice: "))

    if ch == 1:
        c = float(input("Temperature: "))
        print((c * 9 / 5) + 32)

    elif ch == 2:
        f = float(input("Temperature: "))
        print((f - 32) * 5 / 9)

    else:
        print("Invalid Choice")


def password():
    p = input("Enter password: ")

    score = 0

    if len(p) >= 8:
        score += 1

    if any(i.isupper() for i in p):
        score += 1

    if any(i.islower() for i in p):
        score += 1

    if any(i.isdigit() for i in p):
        score += 1

    if score == 4:
        print("Strong Password")
    elif score >= 2:
        print("Medium Password")
    else:
        print("Weak Password")


def guess():
    number = random.randint(1, 50)

    while True:
        g = int(input("Guess Number: "))

        if g == number:
            print("Correct")
            break

        elif g > number:
            print("Too High")

        else:
            print("Too Low")


def add_student():
    roll = input("Roll No: ")

    if roll in students:
        print("Already Exists")
        return

    name = input("Name: ")
    marks = float(input("Marks: "))

    students[roll] = [name, marks]

    print("Added")


def display_students():

    if len(students) == 0:
        print("No Records")
        return

    print("\nRoll\tName\tMarks")

    for roll in students:
        print(roll, "\t", students[roll][0], "\t", students[roll][1])


def update_student():
    roll = input("Roll No: ")

    if roll in students:
        marks = float(input("New Marks: "))
        students[roll][1] = marks
        print("Updated")
    else:
        print("Not Found")


def delete_student():
    roll = input("Roll No: ")

    if roll in students:
        del students[roll]
        print("Deleted")
    else:
        print("Not Found")


def save_file():

    f = open("students.txt", "w")

    for roll in students:
        f.write(
            roll + "," +
            students[roll][0] + "," +
            str(students[roll][1]) + "\n"
        )

    f.close()

    print("Saved")


def load_file():

    try:
        f = open("students.txt", "r")

        students.clear()

        for line in f:
            data = line.strip().split(",")
            students[data[0]] = [data[1], float(data[2])]

        f.close()

        print("Loaded")

    except:
        print("File Not Found")


while True:

    print("\n========== PYTHON PRACTICE ==========")
    print("1. Calculator")
    print("2. Factorial")
    print("3. Fibonacci")
    print("4. Prime Number")
    print("5. Palindrome")
    print("6. Armstrong Number")
    print("7. Even Odd Counter")
    print("8. Largest Smallest")
    print("9. Bubble Sort")
    print("10. Linear Search")
    print("11. Temperature Converter")
    print("12. Password Checker")
    print("13. Number Guessing Game")
    print("14. Add Student")
    print("15. Display Students")
    print("16. Update Student")
    print("17. Delete Student")
    print("18. Save File")
    print("19. Load File")
    print("20. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        factorial()

    elif choice == "3":
        fibonacci()

    elif choice == "4":
        prime()

    elif choice == "5":
        palindrome()

    elif choice == "6":
        armstrong()

    elif choice == "7":
        even_odd()

    elif choice == "8":
        largest_smallest()

    elif choice == "9":
        bubble_sort()

    elif choice == "10":
        linear_search()

    elif choice == "11":
        temperature()

    elif choice == "12":
        password()

    elif choice == "13":
        guess()

    elif choice == "14":
        add_student()

    elif choice == "15":
        display_students()

    elif choice == "16":
        update_student()

    elif choice == "17":
        delete_student()

    elif choice == "18":
        save_file()

    elif choice == "19":
        load_file()

    elif choice == "20":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")