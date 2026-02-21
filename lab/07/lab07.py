"""
Kenneth Huang
Feb 19, 2026
Lab 7 | Working with data in Python
"""

print("Example 1 | Reading Files")
with open("phrases.txt", "r") as file:
    file_content = file.read()
    print(file_content)

# Check if File has closed
print(f"File closed? {file.closed}")

print("Example 2 | File.readline()")
with open("phrases.txt", "r") as file:
    file_content = file.readline(30)
    print(file_content)
    file_content = file.readline(5)
    print(file_content)

print("Example 3 | File.readlines()")
with open("phrases.txt", "r") as file:
    file_content = file.readlines()
    print(file_content)

print("Example 4 | Looping through file content")
with open("phrases.txt", "r") as file:
    for line in file:
        print(line)

print("Example 5 | Create File")
with open("huang.txt", "w") as file:
    file.write("Python basics for data science\n")
    file.write("Kenneth Huang\n")

print("Example 6 | Append Data to Existing File")
with open("huang.txt", "a") as file:
    from datetime import datetime
    file.write(f"Last update: {datetime.now()}\n")

print("Example 7 | Copy a File")
with open("huang.txt", "r") as original:
    with open("huang(1).txt", "w") as copy:
        for line in original:
            copy.write(line)

print("Example 8 | Pandas")
import pandas 
data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age":  [25, 30, 35],
}

df = pandas.DataFrame(data)
print(df)

print("Example 9 | Creating pandas.Datarame with an .xlsx/.csv file")  # I don't have .xlsx so .csv it is
df = pandas.read_csv("data.csv")
print(df)
print(df.head())

print("Exercise")

def email_read():
    gmail = 0
    yahoo = 0
    hotmail = 0

    with open("./user_email.txt", "r") as file:
        for user in file:
            email_provider = user.split("@")[1].split(".")[0]
            if email_provider == "gmail":
                gmail += 1
            elif email_provider == "yahoo":
                yahoo += 1
            elif email_provider == "hotmail":
                hotmail += 1

    return (gmail, yahoo, hotmail)

print(email_read())
