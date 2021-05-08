def main():
    student_list = [['Harry', 37.21], ['Berry', 37.21],
                    ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    sorted_student_list = sorted(
        student_list,
        key=lambda student: student[1],
        reverse=True)

    second_last_list = []
    second_last_grade = sorted_student_list[-2][1]

    for grade in sorted_student_list:
        if grade[1] == second_last_grade:
            second_last_list.append(grade)

    final_student_list = sorted(second_last_list)

    for name in final_student_list:
        print(name[0])


if __name__ == "__main__":
    main()
