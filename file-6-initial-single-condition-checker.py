# userName = input("Please enter your name ? ")
# print("Username is: " + userName)

userAge = input("Please enter age ? ") # userAge="21" # which is a str

#validation


print("User age is: " + userAge) # userAge is still str

print(type(userAge)) # <class 'str'> line 11


oldAge = int(userAge)+6 # now userAge is type = int (integer, not string)
type(oldAge)
print(f"in 5 years you will be {oldAge}")
