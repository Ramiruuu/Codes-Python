while True:
    print("Type 'exit' to stop: ", end="")  # Ensures better input handling
    user_input = input()
    if user_input.lower() == "exit":
        print("Exiting loop...")
        break
    print("You entered:", user_input)