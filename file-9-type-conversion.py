userName = input("Enter username:")
print(type(userName))
print("Username is: " + userName)
userAge= input("Please enter your age ? ")
print("Use age is:" + userAge)
# str to int
# https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=To%20convert%2C%20or%20cast%2C%20a,of%20the%20value%20you%20passed.
intAge=int(userAge)
oldAge=6
addedAge=intAge+oldAge
print("in 5 years you will be:", addedAge)
