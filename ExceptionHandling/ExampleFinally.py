user_input: str = input("Enter a Number:")

try:
    number = float(user_input)
    print(number)
except Exception as e:
    print("Exception", e)
else:
    print("Code run successfully")
finally:
    print("This will run always")
