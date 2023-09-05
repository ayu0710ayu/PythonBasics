user_input=input("Enter a Number:")

try :
    number=float(user_input)
    print(number)
except ValueError:
    print("please enter a valid no.")
