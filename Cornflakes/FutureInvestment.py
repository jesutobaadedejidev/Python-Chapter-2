def future_investment(investment_amount, monthly_interestRate, numberOfMonths):
	future_investment_value = investment_amount*(1+monthly_interestRate)**numberOfMonths
	return future_investment_value

amount = int(input("Enter the investment amount: "))
interest = int(input("Enter the monthly interest rate: "))
months = int(input("Enter the number of months: "))

result = future_investment(amount, interest, months)
print(result)

