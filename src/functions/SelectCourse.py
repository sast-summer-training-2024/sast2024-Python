def list_all_courses(courses):
    print(
        "---------------------------------------------------------------------------------------------------------------course info---------------------------------------------------------------------------------------------------------------\n",
        "          Id                                                  Name                                                                       Teacher                                                          Department                                                  Time             ")
    tqlk = "{: ^10}\t{: ^50}\t{: ^40}\t{: ^40}\t{: ^40}"
    for course in courses:
        print(tqlk.format(course["id"], course["name"], course["teacher"], course["department"], course["time"]))
    return


def select_course(student, courses):
    list_all_courses(courses)
    print("Please enter the course id you want to selected:")
    course_id = input()
    if course_id in student[0]["selected"]:
        print("The course has been selected")
    for course in courses:
        if course["id"] == course_id:
            for selected_course_id in student[0]["selected"]:
                for course_selected in courses:
                    if course_selected["id"] == selected_course_id:
                        if (course_selected["time"][:3] == course["time"][:3] and
                                not (int(course_selected["time"][4:6]) >= int(course["time"][10:12]) or
                                     int(course_selected["time"][10:12]) <= int(course["time"][4:6]))):
                            print("The course you select has time-confliction with your selected course")
                        else:
                            print("Course selected successfully!")
                            student[0]["selected"].append(course["id"])
    return
