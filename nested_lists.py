def main():
    student_list = [['Harry', 37.21], ['Berry', 37.21],
                    ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    second_last = sorted(
        list(set(grade for name, grade in student_list)), reverse=True)[-2]

    second_last_list = []

    for name in student_list:
        if name[1] == second_last:
            second_last_list.append(name[0])

    ordered_list = sorted(second_last_list)

    for name in ordered_list:
        print(name)

if __name__ == "__main__":
    main()
