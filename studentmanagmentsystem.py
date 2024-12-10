# Function to retrieve student info
def retrieve_student_info():
    students_grades = {}
    while True:
        name = input("Enter your name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try: 
            grade = float(input(f"Enter your grade for {name}: "))
            students_grades[name] = grade
        except ValueError:
            print("Invalid input. Please enter a number")
        return students_grades

# Function to calculate the grades

def calculate_grades(students_grades):
    if not students_grades:
        return None
    
    average_grade = sum(students_grades.values()) / len(students_grades)
    best_student = max(students_grades, key= students_grades.get)
    worst_student = min(students_grades, key= students_grades.get)
    return {
        'average' : average_grade,
         'best ': (best_student, students_grades[best_student]),
         'worst' : (worst_student, students_grades[worst_student])
    }
# Function to print the results
def print_results(student_grades, statistics):
    if not student_grades:
        print("No student data to display.")
        return
    
    print("\n--- Student Grades ---")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

    print("\n--- Statistics ---")
    print(f"Average Grade: {statistics['average']:.2f}")
    print(f"Highest Grade: {statistics['highest'][0]} ({statistics['highest'][1]})")
    print(f"Lowest Grade: {statistics['lowest'][0]} ({statistics['lowest'][1]})")

# Main Program
if __name__ == "__main__":
    student_grades = retrieve_student_info()
    statistics = calculate_grades(student_grades)
    print_results(student_grades, statistics)