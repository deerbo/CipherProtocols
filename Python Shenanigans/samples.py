print("\nHello World!\n")

# Ask the user for their name and age, then print:
# "Hello [name], you are [age] years old."
def nameAndAge():
    name = input("type in your name\n")
    age = input("type in your age\n")
    print("Hello " + name + ", you are " + str(age) + " years old.")

#Write a program that takes a number from the user and prints whether it’s even or odd.
def evenOrOdd():
    num = int(input("type in a number\n"))
    if (num % 2) == 0:
        print("The number is even")
    else:
        print("The number is odd")

#Take two numbers and an operator (+, -, *, /) from the user and perform the calculation.
def simpleCalc():
    num1 = float(input("type first num\n"))
    op = str(input("type op\n"))
    num2 = float(input("type second num\n"))
    if "+" == op:
        sum = num1 + num2
    elif "-" == op:
        sum = num1 - num2
    elif "*" == op:
        sum = num1 * num2
    else:
        if num2 == 0:
            print("divide by 0 error")
        else:
            sum = num1 / num2
        
    if sum.is_integer(): print(int(sum)) 
    else: print(sum)

# Print the first n Fibonacci numbers (ask the user for n).        
def fibonacci():
    num1 = 0
    num2 = 1
    num3 = 0
    n = int(input("how many fibonacci nums do you want?\n"))
    for x in range(n):
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3

def listReverser(lst):
    count = 0
    for elem in range(int(len(lst)/2)):
        save = lst[count]
        lst[count] = lst[len(lst) - count - 1]
        lst[len(lst) - count - 1] = save 
        count += 1
    print(lst)

