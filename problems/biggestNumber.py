
def validate_input( message: str):
    try:
        x = input(message)
        number = int(x)
        return number
    except:
        print("Input is not a number")
        validate_input(message)



first_input = validate_input("Enter first number: ")
second_input = validate_input("inpute second number")
third_input = validate_input("inpute third number")


def formatedPrint(input):
    print(f"Biggest number : {input}")



if first_input > second_input and first_input > third_input:
    formatedPrint(first_input)
elif first_input < second_input and second_input > third_input:
    formatedPrint(second_input)
else:
    formatedPrint(third_input)



