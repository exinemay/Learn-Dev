command = ""
while command.lower() != "quit":
    command = input('> ')

    if command.lower() == "start":
        print("Car started...")
    elif command.lower() == "stop":
        print("Car stopped!")
    elif command.lower() == "help":
        print("""Start - To start the car
Stop - To stop the car
quit - To quit""")
    elif command.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand that!")