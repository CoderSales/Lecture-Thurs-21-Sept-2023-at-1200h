username = input("enter your name:")
userAge = int(input("enter your age:"))
userSem = int(input("enter your semester 1 or 2:"))

print("Username is: " + username)
print("Your age is: " + str(userAge))
print("Your semester is: " + str(userSem))

# if userAge >= 18 :
#    if userSem !=1:
#        print("Have a beer ")
#        print("It going to be a nice day ")

if userAge >= 18 and userSem != 1:
  if userSem != 1:
      print("Have a beer ")
      print("It going to be a nice day")

print('good bye!! ')
