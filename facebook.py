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
    print(int(first_number)+int(second_number))
if oparator=="-":
    print(int(first_number)-int(second_number))
if oparator=="*":
    print(int(first_number)*int(second_number))
if oparator=="/":
    if second_number=="0":
        print("any number has not divided by o")
    else:
        print(int(first_number)/int(second_number))

