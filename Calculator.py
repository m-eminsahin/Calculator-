def calculator(Number1, Number2, action):
    if action not in "+ - * /":
        return "make sure that you have entered the correct action"

    if action == "+":
        return (str(Number1) + " + " + str(Number2) + " = " + str(Number1 + Number2))
    if action == "-":
        return (str(Number1) + " - " + str(Number2) + " = " + str(Number1 - Number2))
    if action == "*":
        return (str(Number1) + " * " + str(Number2) + " = " + str(Number1 * Number2))
    if action == "/":
        return (str(Number1) + " / " + str(Number2) + " = " + str(Number1 / Number2))


while True:
    try:
        Number1 = int(input("Enter a number: "))
        Number2 = int(input("Enter a number: "))
        action = input("+ - * /")
        print(calculator(Number1, Number2, action))
    except:
        print("make sure you have entered the correct number")

