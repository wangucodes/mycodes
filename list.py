classmates = ["priya", "aarav", "dev", "wangu", "tia"]
print("class list:", classmates)
print("total students:", len(classmates))
print("first student:", classmates[0])
print("last student:", classmates[-1])
print("First three:", classmates[:3])
classmates.append("meera")
print("\nAfter adding meera:", classmates)
classmates.remove("dev")
print("\nAfter removing dev:", classmates)
classmates.sort()
print("sorted alphabetically:", classmates)
classmates.reverse()
print("reversed:",classmates)
teacher = {"name": "mr.sharma", "subject": "python", "experience": "5"}
print("\nTeacher profile:", teacher)
print("subject:", teacher["subject"])
print("experience:", teacher.get("experience, Not found"))
teacher["experience"] = 6
teacher["email"] = "sharmmaschool.com"
teacher.pop("experience")
print("updated teacher profile:", teacher)
roll_number = [1, 2, 3, 4, 5]
names = ["priya", "dev", "meera", "tia", "aarav"]
d = dict(zip(roll_number, names))
print("\n student dictionary:", d)
print("\n student at roll_number 3:", d)