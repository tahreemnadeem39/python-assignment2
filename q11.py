#Q11-Get a List
def get_user_values() -> None:
    
    values: list[str] = []

    while True:
        user_input = input("Enter a value: ")

        if user_input == "":
            break

        # Add the input value to the list
        values.append(user_input)

    print("Here's the list:", values)

# Call the function 
get_user_values()
