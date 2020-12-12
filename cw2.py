print("Lesson-1. Working with varibales")

s = "stroke"  #строка
a = 5
b = 1.1
t = False

lst = [1, 2, 3]
st = {1, 2, 3}
d = {1: 'asdfsd', 2: '7364767364'}

res = a + b
result =f"Variables: String: {s}, Integer: {a}, Float: {b}, Boolean: {t}, a Value of operation: {res}"
print(result)

name = input("Enter Name:")
age = input("Enter the age:")
gender = input("Enter a gender:")

result = "User info:"+" "+name+" "+age+" "+gender
print(result)

result = f"User info: {name} {age} {gender}"
print(result)

age = int(age)
print("User info: %s %d %s" % (name, age, gender))

print(age == 29 and name == "Timur")

action = "sleep"
while (action != "?"):
    if action == "sleep":
        print("Safe sleep!")
    if action == "play":
        print("good game")
    if action == "eat":
        print("best eating")
    action = input("Что делаешь? ")
    if action == "sleep":
        print(1)
    elif action == "play":
        print(2)
    elif action == "eat":
        print(3)

time_=input("Enter the time (in seconds): ")
print(f"Time is: {time_ // 3600}<2:{time_ // 60}")
