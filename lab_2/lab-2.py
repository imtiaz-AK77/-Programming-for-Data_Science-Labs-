progamming_for_ds = float(input("ent your program for ds mark: "))

data_visualization = float(input("ent your data visualiza mark: "))

data_processing = float(input("ent your data processing mark: "))

data_mining = float(input("ent your data mining mark: "))

java = float(input("ent your java mark: "))

marks = [progamming_for_ds, data_visualization, data_processing, data_mining, java]

total_marks = 0
for mark in marks:
    total_marks += mark

#print(sum(marks))
print(f"Total marks: {total_marks}")

hight_mark = 0
for mark in marks:
    if mark > hight_mark:
        hight_mark = mark

print(f"Highest mark: {hight_mark}")

lower_mark = marks[0]
for mark in marks:
    if mark < lower_mark:
        lower_mark = mark

print(f"Lowest mark: {lower_mark}")
print(f"Average mark: {total_marks / len(marks)}")

passed_courses = [mark for mark in marks if mark >= 50]
print(f"Number of passed courses: {len(passed_courses)} out of {len(marks)}")


