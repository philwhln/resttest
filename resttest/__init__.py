from resttest import display, transactions


def run():
    running_total = transactions.ZERO
    daily_balances = transactions.all_daily_balances()
    for date in sorted(daily_balances.keys()):
        days_total = daily_balances[date]
        running_total += days_total
        display.print_running_daily_balance(date, days_total, running_total)

    print('')
    grand_total = transactions.grand_total(daily_balances)
    display.print_grand_total(grand_total)
