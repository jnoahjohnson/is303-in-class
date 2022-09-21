# Return the letter grade based on the numeric grade (0-100)
def get_letter_grade(grade):
    returnGrade = ""

    if grade >= 90:
        returnGrade = "A"
    elif grade >= 80:
        returnGrade = "B"
    else:
        returnGrade = "C"

    return returnGrade