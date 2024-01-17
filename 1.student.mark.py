# function input number of students
def input_num_of_students():
    return int(input("Enter the number of student in the class: "))

# function input information of students
def input_student_information():
    return (
        input("Enter student ID: "),
        input("Enter student name: "),
        input("Enter student date of birth: ")
    )

# function input number of courses
def input_num_of_courses():
    return int(input("Enter the number of courses: "))

# function input information of courses
def input_course_information():
    return (
        input("Enter course ID: "),
        input("Enter course name: ")
    )

# function input mark of students
def input_student_marks(students):
    course_id = input("Enter the course ID: ")
    courses_marks = {}
    for student in students:
        mark = float(input(f"Enter the mark for student {student[1]}: "))
        courses_marks[student[0]] = mark
    return (course_id, courses_marks)

# function list course
def list_courses(courses):
    print("Courses: ")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

# function list student
def list_students(students):
    print("Student: ")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

# function to show mark
def show_student_marks(students, marks):
    course_id = input("Enter the courses ID: ")
    print("Student marks: ")
    for student in students:
        if student[0] in marks[course_id]:
            mark = marks[course_id][student[0]]
            print(f"Student: {student[1]}, Mark: {mark}")

def main():
    # input the number of student 
    num_student = input_num_of_students()

    # list of students
    students = []
    for _ in range (num_student):
        student_info = input_student_information()
        students.append(student_info)

    # input the number of course
    num_course = input_num_of_courses()

    # list of courses
    courses = []
    for _ in range (num_course):
        courses_info = input_course_information()
        courses.append(courses_info)

    # dictionary of marks
    marks = {}
    for course in courses:
        marks[course[0]] = {}
        marks[course[0]] = input_student_marks(students)

    list_courses(courses)
    list_students(students)

    show_student_marks(students, marks)
    
# call the main function
if __name__ == "__main__":
    main()