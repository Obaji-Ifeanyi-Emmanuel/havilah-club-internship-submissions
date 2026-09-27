greeting = "Hello world"
new_greeting = greeting.replace("Hello", "Hi")
print(new_greeting)
dashed_name = "micheal-obaji-ify"
names = dashed_name.split("-")
print(names)

dashed_name = ["micheal", "obaji", "ify"]
join_names = "-".join(names)
print(join_names)

developer = "Cosmas" 
print(developer.startswith("C"))
print(developer.endswith("C"))

filename = "student.CSV"
if filename.endswith(".CSV"):
    print("This is a CSV file")

else:
    print("cannot identify file")

developer = "Cosmas" 
print(developer.find("m"))
print(developer.find("f"))
print(developer.find("m"))

department = "Mechanical Engineering"
print(department.count("e"))

message = " Python is fun. Python is easy"
print(message.count("python"))

favorite_food = "OKPA IS MY FAVORITE FOOD"
print(favorite_food.capitalize())

favorite_food = "OKPA IS MY FAVORITE FOOD"
print(favorite_food.title())

faculty = "ENGINEERING"
print(faculty.lower())

faculty = "ENGINEERING"
print(faculty.isupper())

c:\Users\OBAJI IFEANYI\Downloads\newtexxt - Sheet1.csv