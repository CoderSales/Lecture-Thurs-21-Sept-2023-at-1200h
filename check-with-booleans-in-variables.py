# name
#age
# you can have a beer
# or you cannot have a beer
# (check if >=18 )


name=input('what is your name? :')
age=input('what is your age?:')
ageInt=int(age)

# Part1: check1:
ageCheck=None

if(ageInt>=18):
    ageCheck=True
else:
    ageCheck=False
# print("ageCheck:",ageCheck)


# Part2: check 2:
semester=int(input("What semester?:"))
print(type(semester))

if(semester>1):
    semesterCheck=True
# elif:
#     sadf
# elif:
#     asdf
# elif:
#     asddf
else:
    semesterCheck=False

# Part 3: assemble:

# print("semesterCheck",semesterCheck)
# iff both True say :


if (ageCheck&semesterCheck):
    print('you CAN have a beer')
else:
    print('you CANNOT have a beer because at least one of the 2 conditions failed:')
    print("ageCheck: ", ageCheck)
    print("semesterCheck:", semesterCheck)
