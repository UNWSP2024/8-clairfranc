# Claire Francis, March 20th, 2025, Week8_program5.py

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.


course_info = dict()

def add_course():
    check = True
    while(check == True):
        answer = input("Do you want to add another course? (Input 'yes' for yes, input 'no' for no)")
        if answer == 'yes':
            get_course_number = input("Enter course ID: ")
            get_name = input("Enter course name: ")

            course_subject = get_course_number.split()[0]

            course_info[get_course_number] = [course_subject, get_name, get_course_number]
            print(course_info)

        else:
            check = False
            get_user_input = input("Enter subject: ")
            for val in course_info.values():
                if(val[0] == get_user_input):
                    print(val[1], " ", val[2])






if __name__ == '__main__':
    add_course()




