def print_running_daily_balance(date, days_total, running_total):
    print('{} {:>15} {:>15}'.format(date,
                                    '$' + str(days_total),
                                    '$' + str(running_total)))


def print_grand_total(total):
    print('{:>42}'.format('TOTAL $' + str(total)))
