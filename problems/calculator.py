first_input=input("Enter first number: ")
first_number = int(first_input)

oparator=input("Enter a oparator (+,-,*,/): ")

second_input=input("Enter second input: ")
second_number = int(second_input)



if oparator == "+":
    sum = first_number + second_number
    print(f"{first_number} {oparator} {second_number} = {sum}")
elif oparator == "-":
    sub = first_number - second_number
    print(f"{first_number} {oparator} {second_number} = {sub}")
elif oparator == "*":
    mul = first_number * second_number
    print(f"{first_number} {oparator} {second_number} = {mul}")
elif oparator == "/":
    if second_number == 0:
        print("any number has not divided by o")
    else:
        divition = first_number / second_number
        print(f"{first_number} {oparator} {second_number} = {divition}")
else:
    print("It is not a valid oparator")
