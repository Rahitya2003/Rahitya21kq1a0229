def print_course_details(course_details):
    print("-" * 97)
    print("| {:<25} | {:<12} | {:<20} | {:<10} | {:<25} |".format("Course Name", "Fee", "Enrolled Students", "Seats Left", "Course Duration"))
    print("-" * 97)
    for course in course_details:
        name, fee, enrolled, total_seats, duration = course
        seats_left = total_seats - enrolled
        print("| {:<25} | ${:<11.2f} | {:<16} | {:<10} | {:<25} |".format(name, fee, enrolled, seats_left, duration))
    print("-" * 97)

def print_course_details_specific(course_details, course_name):
    for course in course_details:
        if course[0].lower() == course_name.lower():
            print("\nCourse Details:")
            print(f"Name: {course[0]}")
            print(f"Fee: ${course[1]:.2f}")
            print(f"Enrolled Students: {course[2]}")
            print(f"Seats Left: {course[3] - course[2]}")
            print(f"Course Duration: {course[4]}")
            return
    print("Course not found.")

def query_course_fee(course_details, course_name):
    for course in course_details:
        if course[0].lower() == course_name.lower():
            print(f"The fee for {course_name} is ${course[1]:.2f}")
            return
    print("Course not found.")

def query_courses_enrollment(course_details):
    print("\nEnrollment Details for Each Course:")
    for course in course_details:
        print(f"{course[0]}: Enrolled students - {course[2]}, Seats left - {course[3] - course[2]}")

def check_course_existence(course_details, course_name):
    for course in course_details:
        if course[0].lower() == course_name.lower():
            return True
    return False

def query_seats_left(course_details):
    print("\nSeats Left for Each Course:")
    for course in course_details:
        seats_left = course[3] - course[2]
        print(f"{course[0]}: {seats_left} seats left")

def query_courses_under_50_seats(course_details):
    count = 0
    print("\nCourses with Intake Less Than 50 Seats:")
    for course in course_details:
        if course[3] < 50:
            count += 1
    print(f"Total Courses with Intake Less Than 50 Seats: {count}")

def query_total_filled_seats(course_details):
    total_filled_seats = sum(course[2] for course in course_details)
    print(f"\nTotal Filled Seats Across All Courses: {total_filled_seats}")


def query_courses_over_1000_fee(course_details):
    count = 0
    print("\nCourses with Fee Greater Than $1000:")
    for course in course_details:
        if course[1] > 1000:
            count += 1
    print(f"Total Courses with Fee Greater Than $1000: {count}")
def query_courses_less_1000_fee(course_details):
    count = 0
    print("\nCourses with Fee less than Than $1000:")
    for course in course_details:
        if course[1] < 1000:
            count += 1
    print(f"Total Courses with Fee less than Than $1000: {count}")

def query_total_courses(course_details):
    print(f"\nTotal Number of Courses: {len(course_details)}")

def query_total_seats(course_details):
    total_seats = sum(course[3] for course in course_details)
    print(f"\nTotal Number of Seats Across All Courses: {total_seats}")


def main():
    course_details = []
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        print(f"\nEnter details for Course {i+1}:")
        name = input("Enter course name: ")
        while True:
            try:
                fee = float(input("Enter course fee: $"))
                enrolled = int(input("Enter number of enrolled students: "))
                total_seats = int(input("Enter total number of seats: "))
                duration = input("Enter course duration: ").strip()
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        course_details.append((name, fee, enrolled, total_seats, duration))
    print("\nCourse Details:\n")
    print_course_details(course_details)
    while True:
        option = input("\nEnter '1' to query course fee, '2' to query available seats, '3' to display specific course details, '4' to check course existence, '5' for enrollment details,'6' total filled seats,'7' course fee >1000$,'8' total courses,'9' course fee <1000$, '10' total seats or 'q' to quit: ").strip().lower()
        if option == '1':
            course_name = input("Enter the name of the course to display fee: ").strip()
            query_course_fee(course_details, course_name)
        elif option == '2':
            query_courses_enrollment(course_details)
        elif option == '3':
            course_name = input("Enter the name of the course to display details: ").strip()
            print_course_details_specific(course_details, course_name)
        elif option =='4':
            course_name=input("Enter the name of the course to check existence: ").strip()
            if check_course_existence(course_details, course_name):
                print(f"The course '{course_name}' exists.")
            else:
                print(f"The course '{course_name}' does not exist.")
        elif option =='5':
            query_courses_under_50_seats(course_details)
        elif option == '6':
            query_total_filled_seats(course_details)
        elif option == '7':
            query_courses_over_1000_fee(course_details)
        elif option == '8':
            query_total_courses(course_details)
        elif option=='9':
            query_courses_less_1000_fee(course_details)
        elif option == '10':
            query_total_seats(course_details)
        elif option == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
