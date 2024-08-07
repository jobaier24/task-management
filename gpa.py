subject_number = int(input("Subject number: "))

marks = []

for i in range(0,subject_number):
    number = int(input("Enter your subject mark: "))
    marks.append(number)
    





# get average
sum = 0
for mark in marks:
    sum = sum + mark
    # print(mark)

# print("Summation of ",marks, "=",sum )
avg = sum / len(marks)

#  continally print grade

if avg < 33:
    print("You failed")
elif avg >= 33 and avg < 40:
    print("You got D")
elif avg >= 40 and avg < 50:
    print("You got C")
elif avg >= 50 and avg < 60:
    print("You got A-")
elif avg >= 60 and avg < 70:
    print("you got A")
elif avg >= 70 and avg < 80:
    print("You got A")
elif avg >= 80:
    print("You got A+")