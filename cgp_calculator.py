course_count = int(input("How many courses are you offering?: "))
unit_list = []
weighted_scores_list = []

for count in range(0, course_count):

    score = int(input("Enter next score: "))
    unit = int(input("Enter above course unit: "))

    if score > 69:
        grade = "A"
        grade_int = 5.0
    elif score > 59:
        grade = "B"
        grade_int = 4.0
    elif score > 49:
        grade = "C"
        grade_int = 3.0
    elif score > 44:
        grade = "D"
        grade_int = 2.0
    elif score > 39:
        grade = "E"
        grade_int = 1.0
    elif score < 40:
        grade = "F"
        grade_int = 0.0

    weighted_score = grade_int*unit
    unit_list.append(unit)
    weighted_scores_list.append(weighted_score)

    print(weighted_score)
    print(f"Your grade: {grade}")

gpa = sum(weighted_scores_list)/sum(unit_list)
print(gpa)

