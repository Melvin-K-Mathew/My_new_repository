def payroll():
    basic = int(input("Please enter the amount received as Basic Salary\n"))
    hra = int(input("Please enter the amount received as House Rent Allowance\n"))
    other = int(input("Please enter the amount received as Allowances for any other facilities\n"))

    # Gross salary is the sum o the basic, HRA and other allowances received
    gross_salary = basic + hra + other
    print(gross_salary, "is the total amount received as gross salary")
    tot_days = int(input("Please enter the total number of working days\n"))
    leave = int(input("Please enter the days the employee has taken leave\n"))
    pay_ded = (gross_salary / tot_days) * (leave)
    salary = gross_salary - pay_ded
    print("the salary to be paid for the employee is", salary)

i=1
while i==1:

    f = open("Payroll.txt", "a")
    f.close()
    name=str(input("Please enter the name of the employee\n"))
    add=str(input("Please enter the address of the employee\n"))
    e_mail=str(input("Please enter the Mail ID of the employee\n"))
    ph_no=str(input("Please enter the Phone number of the employee\n"))
    payroll()
    i=int(input("Press 1 if you would like to make another calculation else press 0\n"))