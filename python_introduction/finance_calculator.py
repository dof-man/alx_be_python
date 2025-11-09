monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
savings = monthly_income - monthly_expenses
interest_rate = 0.05
projected_savings = (savings * 12 + (savings * 12 * 0.05))
print("Your monthly savings are", monthly_income - monthly_expenses)
print("Projected savings after one year, with interest, is:", projected_savings) 