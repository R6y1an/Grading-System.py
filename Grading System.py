def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid Score'

def main():
    try:
        score = float(input("Enter the student's score: "))
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")
    except ValueError:
        print("Invalid input. Please enter a numerical score.")

if __name__ == "__main__":
    main()

    






    






    



