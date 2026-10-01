import math
import numpy as np


# ==========================================
# INPUT FUNCTIONS
# ==========================================

def input_students():
    students = []

    number_of_students = int(input("Enter number of students: "))

    for i in range(number_of_students):
        print(f"\n--- Student {i + 1} ---")

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


def input_courses():
    courses = []

    number_of_courses = int(input("\nEnter number of courses: "))

    for i in range(number_of_courses):
        print(f"\n--- Course {i + 1} ---")

        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))

        course = {
            "id": course_id,
            "name": name,
            "credits": credits
        }

        courses.append(course)

    return courses


def input_marks(students, courses, marks):
    print("\n========== SELECT COURSE ==========")

    for course in courses:
        print(
            f"{course['id']} - "
            f"{course['name']} "
            f"({course['credits']} credits)"
        )

    course_id = input("Select course ID: ")

    # Find selected course
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    # Course does not exist
    if selected_course is None:
        print("Course not found!")
        return

    print(f"\nEnter marks for: {selected_course['name']}")

    # Create dictionary for this course
    marks[course_id] = {}

    # Input mark for every student
    for student in students:

        while True:
            try:
                mark = float(
                    input(
                        f"Enter mark for "
                        f"{student['id']} - {student['name']}: "
                    )
                )

                if 0 <= mark <= 10:

                    # Round-down to 1 decimal place
                    mark = math.floor(mark * 10) / 10

                    break

                else:
                    print("Mark must be between 0 and 10.")

            except ValueError:
                print("Please enter a number.")

        marks[course_id][student["id"]] = mark

    print(
        f"\nMarks for {selected_course['name']} "
        f"saved successfully!"
    )


# ==========================================
# LISTING FUNCTIONS
# ==========================================

def list_students(students):
    print("\n========== STUDENTS ==========")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"DoB: {student['dob']}"
        )


def list_courses(courses):
    print("\n========== COURSES ==========")

    for course in courses:
        print(
            f"ID: {course['id']} | "
            f"Name: {course['name']} | "
            f"Credits: {course['credits']}"
        )


def show_marks(students, courses, marks):
    print("\n========== SELECT COURSE ==========")

    # Show only courses that already have marks
    courses_with_marks = []

    for course in courses:
        if course["id"] in marks:
            courses_with_marks.append(course)

    if len(courses_with_marks) == 0:
        print("There are no courses with marks yet.")
        return

    for course in courses_with_marks:
        print(
            f"{course['id']} - "
            f"{course['name']}"
        )

    course_id = input("Select course ID: ")

    # Check whether selected course has marks
    if course_id not in marks:
        print("No marks for this course!")
        return

    # Find course information
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    print(
        f"\n========== MARKS: "
        f"{selected_course['name']} =========="
    )

    for student in students:

        student_id = student["id"]

        if student_id in marks[course_id]:
            print(
                f"ID: {student_id} | "
                f"Name: {student['name']} | "
                f"Mark: {marks[course_id][student_id]:.1f}"
            )


# ==========================================
# GPA FUNCTIONS
# ==========================================

def calculate_gpa(student, courses, marks):
    """
    Calculate weighted GPA.

    GPA =
        sum(mark * credit)
        ------------------
        sum(credit)
    """

    weighted_marks = []
    credits = []

    for course in courses:

        course_id = course["id"]

        # Check whether marks exist for this course
        if course_id in marks:

            student_id = student["id"]

            # Check whether this student has a mark
            if student_id in marks[course_id]:

                mark = marks[course_id][student_id]
                credit = course["credits"]

                weighted_marks.append(mark * credit)
                credits.append(credit)

    # Student has no marks
    if len(credits) == 0:
        return 0.0

    # Convert lists to NumPy arrays
    weighted_marks = np.array(weighted_marks)
    credits = np.array(credits)

    # Calculate weighted GPA
    gpa = np.sum(weighted_marks) / np.sum(credits)

    return gpa


def show_gpa(students, courses, marks):

    print("\n========== STUDENT GPA ==========")

    students_with_gpa = []

    # Calculate GPA for every student
    for student in students:

        gpa = calculate_gpa(
            student,
            courses,
            marks
        )

        student_result = {
            "id": student["id"],
            "name": student["name"],
            "gpa": gpa
        }

        students_with_gpa.append(student_result)

    # Create NumPy array containing GPA values
    gpa_array = np.array(
        [
            student["gpa"]
            for student in students_with_gpa
        ]
    )

    # Sort GPA from high to low
    sorted_indices = np.argsort(gpa_array)[::-1]

    print(
        f"{'Rank':<6}"
        f"{'ID':<12}"
        f"{'Name':<25}"
        f"{'GPA':<8}"
    )

    print("-" * 51)

    rank = 1

    for index in sorted_indices:

        student = students_with_gpa[index]

        print(
            f"{rank:<6}"
            f"{student['id']:<12}"
            f"{student['name']:<25}"
            f"{student['gpa']:.2f}"
        )

        rank += 1


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    # -----------------------------
    # Input students
    # -----------------------------

    students = input_students()

    # -----------------------------
    # Input courses
    # -----------------------------

    courses = input_courses()

    # -----------------------------
    # Dictionary to store all marks
    # -----------------------------

    marks = {}

    # -----------------------------
    # Main menu
    # -----------------------------

    while True:

        print("\n")
        print("================================")
        print("     STUDENT MARK MANAGEMENT")
        print("================================")
        print("1. Input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks")
        print("5. Show GPA")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            input_marks(
                students,
                courses,
                marks
            )

        elif choice == "2":

            list_students(students)

        elif choice == "3":

            list_courses(courses)

        elif choice == "4":

            show_marks(
                students,
                courses,
                marks
            )

        elif choice == "5":

            show_gpa(
                students,
                courses,
                marks
            )

        elif choice == "6":

            print("Program ended.")
            break

        else:

            print(
                "Invalid choice. "
                "Please try again."
            )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()