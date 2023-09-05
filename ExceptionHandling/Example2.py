user_input=input("Enter a Number:")

try :
    number=float(user_input)
    print(number)
except Exception as e:
    print(e)
