print("Welcome to student info system")
#1. Take user input
full_name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
programme = input("What's your programme of study: ")
level = input("what's your level: ")
age = input("what's your age: ")
programming_language = input("what's your favourite programming language: ")

#2. Generate username and email for user
username = full_name + student_id
email = username + "@st.ug.edu.gh"

# border line
border_line = "="

#3. Give user-friendly output
print(border_line * 45)
print("Student Information")
print(border_line * 45)

print("Full Name: " + full_name)
print("Student ID: " + student_id)
print("Programme: " + programme)
print("Level: " + level)
print("Age: " + age)
print("Programming Language: " + programming_language)
print("Username: " + username)
print("Generated Email: " + email)

print(border_line * 45)
