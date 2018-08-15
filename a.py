import numpy as np
from functions import avg_daily_balances

# account_one = input('Enter Account Name: ')
# account_apr = float(input('Enter Account APR: '))
# account_balance = float(input('Enter Account Balance: '))
# # account_due_date = input('Enter Account Due Date: ')


account_one = "chase"
account_apr = float(0.2999)
account_balance = 200

months_to_pay = 0

while account_balance > 1:
    account_balance = avg_daily_balances(apr=account_apr, bal=account_balance, addtl_pmt=0)
    print(account_balance)
    months_to_pay +=1



print(months_to_pay)


