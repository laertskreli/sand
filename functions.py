# helper functions


def avg_daily_balances(bal, apr, addtl_pmt):

    cumulative_interest = 0

    # APR - based interest payment. Assumes average daily balances method
    interest_calc = (bal * (1 + apr / 365) ** (365 * (1 / 12))) - bal

    # Card act actual minimum payment requirement
    card_act_calc = bal * 0.01

    # Card Act + APR
    minimum_payment = interest_calc + card_act_calc
    print(minimum_payment)

    # Card Act + APR + Additional Payments
    total_deductions = interest_calc + card_act_calc + addtl_pmt

    if minimum_payment < 35:
        minimum_payment = 35
    else: minimum_payment = minimum_payment

    new_bal = bal - total_deductions + interest_calc if bal - minimum_payment > 0 else 0

    return new_bal