print("Test String")

s = "stroke"  #строка
a = 5
b = 1.1
t = False

lst = [1, 2, 3]
st = {1, 2, 3}
d = {1: 'asdfsd', 2: '7364767364'}

res = a + b
print(res)

some_data = input()
print(some_data)

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
    print (3)

while (action = input("?"))