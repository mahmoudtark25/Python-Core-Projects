from math import ceil

def number_of_monthly_payments(loan_principal):
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    number_of_months = loan_principal / monthly_payment
    if number_of_months == 1:
        print(f"It will take {ceil(number_of_months)} month to repay the loan")
    else:
        print(f"It will take {ceil(number_of_months)} months to repay the loan")
    
def monthly_payment(loan_principal):
    print("Enter the number of months:")
    number_of_months = int(input())
    monthly_payment = loan_principal / number_of_months
    last_payment = loan_principal - (number_of_months - 1) * ceil(monthly_payment)
    if monthly_payment == int(monthly_payment):
        print(f"Your monthly payment = {int(monthly_payment)}")
    else:
        print(f"Your monthly payment = {ceil(monthly_payment)} and the last payment = {last_payment}.")
    
print("Enter the loan principal:")
loan_principal = int(input())

print("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:""")
choice = input()
if choice == 'm':
    number_of_monthly_payments(loan_principal)
elif choice == 'p':
    monthly_payment(loan_principal)
