# print("hellow ,worl")
# print("hellow world")
# #Variable:
# a="hellow"
# b="pir hasina"
# print(a+b)

first_number=input("Enter first number: ")
oparator=input("Enter a oparator (+,-,*,/): ")
second_number=input("Enter second input: ")



if oparator=="+":
    sum = int(first_number)+int(second_number)
    print(f"{first_number} {oparator} {second_number} = {sum}")
if oparator=="-":
    sub = int(first_number)-int(second_number)
    print(f"{first_number} {oparator} {second_number} = {sub}")
if oparator == "*":
    mul = int(first_number)*int(second_number)
    print(f"{first_number} {oparator} {second_number} = {mul}")
if oparator=="/":
    if second_number=="0":
        print("any number has not divided by o")
    else:
        divition = int(first_number)/int(second_number)
        print(f"{first_number} {oparator} {second_number} = {divition}")

