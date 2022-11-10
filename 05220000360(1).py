#user informaion inputs
student_no = int(input("Please write your student number:"))
student_name_surname = str(input("Please write your name and your surname:"))

#first courser inputs
first_theoretical_course = int(input("Please write how many hours of the first theoretical course you have:"))
first_practical_couse = int(input("Please write how many hours of the first practical course you have:"))
ECTS_credits_first = int(input("Please write how many ECTS credits of the first course you have:"))
term_grade_first = float(input("Please write your first term grade:"))

#second course inputs
second_theoretical_course = int(input("Please write how many hours of the second theoretical course you have:"))
second_practical_course = int(input("Please write how many hours of the second practical course you have:"))
ECTS_credits_second = int(input("Please write how many ECTS credits of the second course you have:"))
term_grade_second = float(input("Please write your second term grade:"))

#Calculations
local_credits = float(first_theoretical_course + second_theoretical_course + (first_practical_couse/2) + (second_practical_course/2))
ECTS_credits = float(ECTS_credits_first + ECTS_credits_second)
local_credit_WGPA = float((term_grade_first * (first_theoretical_course + (first_practical_couse/2)) / local_credits) +
                          (term_grade_second * (second_theoretical_course + (second_practical_course/2) )) / local_credits)
ECTS_credit_WGPA = float((term_grade_first * ECTS_credits_first / ECTS_credits) + (term_grade_second * ECTS_credits_second / ECTS_credits))

#printings
print("Your student number is:", student_no, "!")
print("Your name is:", student_name_surname, "!")
print("You have", local_credits, "local credits!")
print("You have", ECTS_credits, "ECTS credits!")
print("Your local credit WGPA is:", local_credit_WGPA)
print(f"Your ECTS credit WGPA is: {ECTS_credit_WGPA:.2f}") #if ı dont use .2f it says 3.125



