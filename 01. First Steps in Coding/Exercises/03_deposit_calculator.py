deposit_amount = float(input())
deposit_term_in_months = int (input())
annual_interest_rate = float (input())

accumulated_interest = (deposit_amount * (annual_interest_rate / 100))
monthly_interest = accumulated_interest / 12
total_amount = deposit_amount + (deposit_term_in_months * monthly_interest)

print (total_amount)
