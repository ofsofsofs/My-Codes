# getting user's salary
salary = (int(input("Please enter your salary:")))

# I created names to calculate all data to be collected
person = 0
low_salary = 0
medium_salary = 0
high_salary = 0
total_tax = 0
total_salary = 0
net_total_salary = 0
mega_salary = 0
personal_tax = 0
personal_net_salary = 0

# Here loop is starting to calculate datas after salary entered
while salary > 0:
    # total_tax += personal_tax makes more sense
    person += 1  # calculating people who entered salary
    total_salary += salary  # calculating total salary for outputs
    if 0 < salary <= 10000:  # checking if salary is between 0 and 10000
        low_salary += 1
        personal_tax = salary / 100 * 15
        total_tax += personal_tax  # calculating total tax by adding personal tax
        personal_net_salary = salary / 100 * 85
        net_total_salary += personal_net_salary  # calculating total net salary by adding personal net salary
    elif 10000 < salary < 25000:  # checking if salary is between 10000 and 25000
        medium_salary += 1
        personal_tax = salary / 100 * 20
        total_tax += personal_tax  # calculating total tax by adding personal tax
        personal_net_salary = salary / 100 * 80
        net_total_salary += personal_net_salary  # calculating total net salary by adding personal net salary
    else:  # program use this place if salary is between neither of them
        high_salary += 1
        personal_tax = salary / 100 * 25
        total_tax += personal_tax  # calculating total tax by adding personal tax
        personal_net_salary = salary / 100 * 75
        net_total_salary += personal_net_salary  # calculating total net salary by adding personal net salary
    if salary > 50000:
        mega_salary += 1  # counting person who has more than $50000 salary to calculate percentage

    print(f"Your the amount of income tax to be paid to the state is ${personal_tax:.2f}")  # printing personal tax to be paid
    print(f"Your net salary to be paid to the sales representative is ${personal_net_salary:.2f}")  # printing personal net salary to be paid to representatives
    salary = (int(input("Please enter your salary:")))  # asking salary again for to continue the program

print(f"There are {low_salary:.2f} low salaries, there are {medium_salary:.2f} medium salaries and there are {high_salary:.2f} high salaries.")
print(f"Percentage of sales representatives with a gross salary of more than $50000 among sales representatives with a high gross salary level is %{(mega_salary / high_salary * 100):.2f}")
print(f"Average of all sales representatives' net salary is ${(net_total_salary / person):.2f}")
print(f"The total amount of income tax to be paid to the state is ${total_tax:.2f}")
print(f"The percentage of income tax amount in the total gross salary is %{(total_tax / total_salary * 100):.2f}")
