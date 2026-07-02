# Shilynn Ba-Farlough | Lab 5 | Intro to Python

# Ticket 1

# ages = [17, 11, 25, 13, 9]

# for age in ages :
#     if age >= 13:
#         print(age, "Access Granted")

#     else:
#          print (age, "Too young")

# PREDICT: I think the age greater then 13 will get "Access granted" and the ages less then 13 will get rejected
# EXPLAIN: It holds 17 then goes down the list

# Ticket 3

# while True:
#     age = input("Enter an age or type stop:")
#     if age == "stop":
#         break
#     age = int(age)
#     if age >= 13:
#         print(age, "Access Granted")
#         continue

#     else:
#         print(age, "Too young")

# PREDICT: If you forgot the break statemnet the loop wont end
# EXPLAIN: Ticket 2 loop is on going and this one ends when the age is too young 

# Ticket 4

# def can_access (age):
#     if age >= 13:
#         return True
#     else:
#         return False

# ages = [17, 11, 25, 13, 9]

# for age in ages :
#     if age >= 13:
#         print(age, "Access Granted")

#     else:
#          print (age, "Too young")

# PREDICT: it looks the same but instead of checking the age directly in the loop the code uses the can_access funtion
# EXPLAIN: its better because it stops the code from repeating

# # Ticket 5

# def can_access(age):
#     if age >= 13:
#         return True
#     else:
#         return False
# def signup_report(signups):
#     approved = 0
#     print ("---StreamPass Signup Report---")

#     for number, age in enumerate(signups, start=1):
#         if can_access(age):
#             print(f"Signup #{number} | Age {age} - Acess granted")
#             approved += 1 
#         else:
#              print(f"Signup #{number} | Age {age} - Too young")
#     print(f"Approved: {approved} out of {len(signups)}")

# signups = [22, 10, 15, 8, 19, 13]

# signup_report(signups)

# PREDICT: 4 out of 6
# EXPLAIN: (can_access and signup_report), a list, a for loop, enumerate(), if/else statements, a counter variable (approved), and len() to count the total number of signups.