def do_math():
    user_input = input("Enter a number : ")
    try:
        number = float(user_input)
        print(number)
    except ValueError:
        print("Please enter a Valid Number")
        print("Try again")
        do_math()
    except Exception as e:
        print("Something went wrong")


do_math()
