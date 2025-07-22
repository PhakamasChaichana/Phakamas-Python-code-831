
# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = int(input("Enter age: "))
if age >= 60:
    print("You are an Senior")
elif age >= 20:
    print("You are Adult")
elif age >= 13:
    print("You are Teenager")
else :
    print("You are Child")
